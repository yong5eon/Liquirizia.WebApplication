# Liquirizia.WebApplication
웹 어플리케이션을 개발하기 위한 패키지

## 기본 컴포넌트
* Request : 요청 클래스
* Response : 응답 클래스
* Serializer : 데이터 시리얼라이저

### 데이터 송수신
* RequestReader : 요청 리더
* ResponseWriter : 응답 라이터
* WebSocket : 웹 소켓 리더 및 라이터

### 서버 어플리케이션을 위한 컴포넌트
* RequestRunner : 서버 어플리케이션 인터페이스
* RequestStreamRunner : 스트림 처리를 위한 서버 어플리케이션 인터페이스
* RequestWebSocketRunner : 웹소켓 처리를 위한 서버 어플리케이션 인터페이스
* RequestFilter : 어플리케이션 요청 필터
* RequestFilters : 어프리케이션 요청 필터 어그리게이터
* ResponseFilter : 어플리케이션 응답 필터
* ResponseFilters : 어플리케이션 응답 필터 어그리게이터

### 클라이언트 어플리케이션을 위한 컴포넌트
* ResponseRunner : 클라이언트 어플리케이션 인터페이스

## 사용 예제
* [요청 예제](/sample/WebApplication/Request/Sample.py)
* [응답 예제](/sample/WebApplication/Response/Sample.py)
* [데이터 시리얼라이저 예제](/sample/WebApplication/Serializer/Sample.py)

## TODO
* [ ] RequestWriter : 요청 라이터
* [ ] ResponseReader : 응답 리더
* [ ] WebClientRunner : ResponseRunner 를 활용한 병렬 요청 처리기
* [ ] Encoder 를 Serializer 로 이관