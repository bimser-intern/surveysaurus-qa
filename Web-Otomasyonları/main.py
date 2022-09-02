from signUp import SignUpPage
from login import LoginPage
from fillSurveyWithLogin import FillWithLogin
from fillSurvey import Fill
from comment import CommentPage
from commentWithLogin import CommentWithLoginPage
import sys
from selenium import webdriver


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

if len(sys.argv) == 1:
    sys.exit()

if sys.argv[1] == "production":

    options.add_argument("headless")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--window-size=1920,1080")


if sys.argv[1] == "development":
    # for development
    pass

signup = SignUpPage()
signup.SignUp()

login = LoginPage()
login.Login()

fillsurvey = Fill()
fillsurvey.FillSurvey()

fillSurvey = FillWithLogin()
fillSurvey.FillSurveyWithLogin()

comment = CommentPage()
comment.Comment()

commentpage = CommentWithLoginPage()
commentpage.CommentWithLogin()
