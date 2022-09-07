import modul
from signUp import SignUpPage
from login import Login
from fillSurvey import Fill
from fillSurveyWithLogin import FillWithLogin
from CreateSurvey import Createsurvey
from comment import CommentPage
from commentWithLogin import CommentWithLoginPage
import sys

signup = SignUpPage()
signup.SignUp(modul.driver)

login = Login()
login.Loginsurvey(modul.driver)

fillsurvey = Fill()
fillsurvey.FillSurvey(modul.driver)

fillSurvey = FillWithLogin()
fillSurvey.FillSurveyWithLogin(modul.driver)

create = Createsurvey()
create.createsurvey(modul.driver)

comment = CommentPage()
comment.Comment(modul.driver)

commentpage = CommentWithLoginPage()
commentpage.CommentWithLogin(modul.driver)

sys.exit()