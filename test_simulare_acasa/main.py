from test_simulare_acasa.UI import UI
from test_simulare_acasa.service.students_service import Students_service
from test_simulare_acasa.service.courses_service import Courses_service
from test_simulare_acasa.repository.students_repo import Students_repo

students_repo = Students_repo()

students_service = Students_service(students_repo)
courses_service = Courses_service()


ui = UI(students_service, courses_service)

ui.run()