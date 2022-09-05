from signUp import SignUpPage
from login import login
from fillSurveyWithLogin import FillWithLogin
from fillSurvey import Fill
from CreateSurvey import Createsurvey
from comment import CommentPage
from commentWithLogin import CommentWithLoginPage
import modul
from selenium import webdriver

print("hhh")
options = modul.devops()
driver = webdriver.Chrome(options=options)


signup = SignUpPage()
signup.SignUp()

login = login()
login.Login()

fillsurvey = Fill()
fillsurvey.FillSurvey()

fillSurvey = FillWithLogin()
fillSurvey.FillSurveyWithLogin()

create = Createsurvey()
create.createsurvey()

comment = CommentPage()
comment.Comment()

commentpage = CommentWithLoginPage()
commentpage.CommentWithLogin()
