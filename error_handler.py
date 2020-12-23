""" 예외 처리 통합 관리

모든 레이어에서 raise 되는 예외처리는 이곳에서 처리된다.
각 예외처리에 관한 메세지는 통일성을 위해 이곳에서 정의된대로 사용한다.

자주 사용되는 에러 목록:
    1. InterfaceError, 데이터 조작 할 때 컬럼 개수와 value 개수가 불일치.
    2. DatabaseError, 데이터베이스 시스템 실패.
    3. DataError, 데이터를 집계 불가.(null 불가 필드에 null 입력, 0으로 나누는 연산 등)
    4. OperationalError, 너무 많은 데이터베이스 접속, 데이터소스 이름 없음, 트랜젝션 실행불가, 메모리 할당 에러, 연결 끊김 등 에러.
    5. IntegrityError, 유효하지 않은 cursor, foreignkey 검사 실패로 인한 트랜젝션 실패.
    6. ProgrammingError, SQL 문법에러, 매개변수 수가 불일치.
    7. NotSupportedError, SQL 버전에 맞지 않는 기능 사용 및 SQL 루틴에 맞지 않는 명령실행(rollback 을 끝난 트랜젝션에 요구).

기본적인 사용 예시:
    @app.errorhandler(Exception)
    def handle_error(e):
        return jsonify({'message': 'type your error message here', 'errorMessage': format(e)}), 500

"""

from flask import jsonify
from custom_exceptions import UserAlreadyExist, UserCreateDenied, UserUpdateDenied, UserNotExist, DatabaseCloseFail




# start error handling
def error_handle(app):

    @app.errorhandler(Exception)
    def handle_internal_server_error(e):
        return jsonify({'message': 'internal server error', 'errorMessage': format(e)}), 500

    @app.errorhandler(KeyError)
    def handle_key_error(e):
        return jsonify({'message': 'key error', 'errorMessage': format(e)}), 400

    # customized exception
    @app.errorhandler(UserAlreadyExist)
    def handle_user_already_exist_error(e):
        return jsonify({'message': 'user already exist error', 'errorMessage': format(e)}), 403

    # customized exception
    @app.errorhandler(UserUpdateDenied)
    def handle_user_update_error(e):
        return jsonify({'message': 'user update error', 'errorMessage': format(e)}), 400

    # customized exception
    @app.errorhandler(UserCreateDenied)
    def handle_user_create_error(e):
        return jsonify({'message': 'user create error', 'errorMessage': format(e)}), 400

    # customized exception
    @app.errorhandler(UserNotExist)
    def handle_user_not_exist_error(e):
        return jsonify({'message': 'user does not exist error', 'errorMessage': format(e)}), 400

    # customized exception
    @app.errorhandler(DatabaseCloseFail)
    def handle_database_close_fail_error(e):
        return jsonify({'message': 'unable to close database', 'errorMessage': format(e)}), 400
