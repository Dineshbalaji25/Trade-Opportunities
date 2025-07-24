import os
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.auth import verify_token, create_token
from app.limiter import check_rate_limit
from app.fetch import get_sector_data
from app.model import analyze_with_ai
from app.utils import generate_markdown

router = APIRouter()

# OAuth2 with password flow
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token", scopes={})

# 🔐 Login route to generate JWT token
@router.post("/token", tags=["Authentication"])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    if username == "admin" and password == "admin123":
        access_token = create_token(username)
        return {"access_token": access_token, "token_type": "bearer"}

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )

# 📊 Analyze sector and generate markdown + file
@router.get("/analyze/{sector}", tags=["Trade Analysis"])
async def analyze_sector(
    sector: str,
    token: str = Depends(oauth2_scheme),
):
    # 🔐 Validate token
    user = verify_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")

    # ⛔ Rate limit check
    check_rate_limit(user)

    # 🌐 Get sector data
    raw_data = await get_sector_data(sector)
    if not raw_data:
        raise HTTPException(status_code=404, detail="No data found for sector")

    # 🤖 Run AI analysis
    analysis = await analyze_with_ai(sector, raw_data)

    # 📝 Generate markdown
    markdown = generate_markdown(sector, raw_data, analysis)

    # 💾 Save markdown to file
    reports_dir = "reports"
    os.makedirs(reports_dir, exist_ok=True)
    filename = os.path.join(reports_dir, f"{sector.lower().replace(' ', '_')}_report.md")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(markdown)

    return {
        "sector": sector,
        "report": markdown,
        "file_path": filename
    }
