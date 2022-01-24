---
layout: page
title:  "portfolio"
date:   21-08-22 21:03:36 +0530
last_modified_at: 22-01-20 14:19:00 +0900
categories: Reseacher
---
Portfolio
=========

### 👩‍🎓 Master's Thesis
* Title: [Container Security Framework and MEC Application Relocation for 5G Infrastructure](http://sejong.dcollection.net/common/orgView/200000506160)  

### 👩‍💻 Career  
* [PEL(Protocol Engineering lab)], 석사 과정, 2019.02.01 ~ 2021.08.20
* [Zeppelin], 인턴, 2018.07.30 ~ 2018.08.24
* [PEL(Protocol Engineering lab)], 학부 연구생, 2016.06.27 ~ 2018.02.28  

### 📚 Paper
* Nat. Journal Articles
1. 임연주, 이종혁, “5G MEC 환경에서의 도커 마이그레이션 테스트베드 및 실험 시나리오”, OSIA Standards & Technology Review, Vol. 33, No. 2, pp.26-30, 2020년 9월.  
<br/>
* Nat. Conference Proceedings
1. 박재형, 임연주, 이종혁, “무인항공기 시스템의 제어 통신을 위한 MAVLink 프로토콜 분석”, 한국정보보호학회 충청지부 학술대회, 2021년 8월.
2. 임연주, 이종혁, “컨테이너 환경에서의 이미지 취약점 탐지 및 서명/검증 모델 설계”, 융합스마트미디어 시스템 워크샵(CSMS), 2019년 8월.
3. 최창준, 임연주, 송영준, 이종혁, “이더리움 확장성 문제 해결을 위한 Off-Chain 솔루션 분석”, 한국통신학회 동계종합학술발표회, 2019년 1월.
4. 임연주, 명세인, 권순홍, 이종혁, “블록체인 기반 마이크로그리드 전력거래 시스템”, 한국통신학회 동계종합학술발표회, 2018년 1월.
5. 송영준, 전상기, 임연주, 이종혁, “Shadow Brokers에 의해 유출된 NSA 윈도우 해킹 툴 분석”, 한국정보보호학회 하계학술발표회, 2017년 6월. (우수 논문상 수상)
6. 이부형, 임연주, 이종혁 “블록체인 플랫폼에서의 합의 알고리즘”, 한국통신학회 동계학술발표회, 2017년 1월.  
  
### ✍️ Research Project  
##### Main  
1. 5G Network
	+ 프로젝트명: 저지연 융합서비스를 위한 모바일 에지 컴퓨팅 플랫폼 기술 개발 (with ETRI)
		- 과제 리더 담당
	+ 프로젝트 기간: 2017-04-01 – 2020-12-31 __(4년)__
	+ 기술 스택
		- 5G MEC
			- Kubernetes, Jenkins 
		- Security Framework
			- Signature & Verfication module (자체 개발)
				- Docker, OpenSSL Library, Elasticsearch  
			- Docker Image Vulnerability Diagnostic System
				- [Clair]
		- Container Migration module
			- Helm, Ngnix, Google MAP API
		- 언어: Golang, Python, PHP
	+ 프로젝트 내용
		1. MEC 환경에서의 접근 제어 및 보안 기술 개발  
			- [ETSI 5G MEC](https://www.etsi.org/technologies/multi-access-edge-computing)(Multi-access Edge Computing) 표준 문서 분석
			- 요구사항 분석
			- 도커 컨테이너 이미지 기반 서명 검증 및 취약점 탐지 시스템 설계
			- [Clair] 기반 이미지 취약점 탐지 및 리포팅 서버 개발 
			- Gitlab🦊 기반 취약(악성) 이미지 필터링 모듈 개발 
			- Kubernetes 환경에서 사용 가능한 Docker 기반 이미지 서명/검증 프레임워크 개발(고도화: Docker‘)
		2. 이동성 지원 및 태스크 핸드오프 기술 개발
			- 초저지연을 만족하기 위한 다양한 시나리오 상황에서의 태스크 핸드오프 조건 및 요구사항 분석(Pro-active, Re-active)
			- 컨테이너 기반 Seemless 마이그레이션 아키텍처 설계
			- Kubernetes 기반 Stateful 서비스(Pod) 개발
				- 동영상 스트리밍 서버(Nginx, php)
			- ME Platform 내 UE Location API 기반 태스크 핸드오프 기능 구현 
			- Google Map API를 활용한 UE 이동 정보 시각화 기능 구현
			- 정량적 목표 달성(TTA 시험성적서 발급)
				- MEC 간 태스크 handoff 지연시간 감소율 74.3% 달성
				- 목표치: 20%(1.6초) / 달성: 74.3%(0.514초)

	+ 프로젝트 데모
		- Security Framework
			- [Click😀](https://drive.google.com/file/d/1e4POVJpssNf87_LtxtGoejdRRzunNst9/view?usp=sharing)
		- Container Migration module
			- [Click😁](https://drive.google.com/file/d/1q-oOsti67wMTASD87x77G-kDbx43D-jk/view?usp=sharing)
<br/>  
2. Blockchain 
	+ 프로젝트명: 사설 블록체인 환경에서의 펌웨어 업데이트 아키텍처 연구 및 개발 (with ETRI)  
	+ 기술 스택
		- Hyperledger Fabric, NodeJS, Raspberry Pi 4
		- 언어: Golang, JavaScript
	+ 프로젝트 기간: 2020-04-01 – 2020-10-31
	+ 프로젝트 내용
		- [IETF SUIT](https://datatracker.ietf.org/wg/suit/about/) 표준 문서 분석
		- [IETF 109](https://www.ietf.org/how/meetings/105/) 참석
		- IRTF SCP 프로토콜 상세 분석
		- 하이퍼레저 기반 IoT 펌웨어 업데이트 시스템 설계
		- 하이퍼레저 패브릭 블록체인 네트워크 구성
		- 펌웨어 업데이트를 위한 체인코드 작성
		- NodeJS 기반 SDK 를 이용한 펌웨어 업데이트 Dapp 개발
	+ 프로젝트 데모
		- Register Firmware (Upload)
			- [Click😆](./contents/1.mp4)
		- Update Firmware (Download) 
			- [Click😉](./contents/2.mp4)
<br/>  
<br/>  
	+ 프로젝트명: 마이크로그리드 환경에서의 블록체인 기반 전력거래 시스템 개발 (비공식)
	+ 기술 스택
		- Ethereum, Raspberry Pi 3
		- 언어: Solidity, JavaScript
	+ 프로젝트 기간: 2017-06-01 – 2017-11-30
	+ 프로젝트 내용
		- 합의 알고리즘 분석
		- 이더리움 기반 블록체인 네트워크 구성
		- 트랜잭션 필드 구성(데이터 명세)
		- 스마트 컨트랙트 기반 전력 매매/고객 매칭 자동화 알고리즘 개발(경매 도입)
		- 이더리움 Web3 API 기반 웹용 래퍼함수 개발
		- APM(Apache, PHP, MariaDB) 환경 구축
		- 오픈소스 [PHP-JSON RPC](https://github.com/btelle/ethereum-php) 기반 블록체인 웹 연동
<br/>  

##### All 
<details>
<summary>details (if you want, please click.)</summary>
<div markdown="1">
1. Research on Foundational Technologies for 6G Autonomous Security-by-Design to Guarantee Constant Quality of Security
<br/>Title in Korean: 상시적 보안품질 보장을 위한 6G 자율보안 내재화 기반기술 연구
<br/>Sponsoring Authority: Institute for Information & Communications Technology Promotion (IITP, 정보통신기술진흥센터)
<br/>Duration: 2021-04-01 – 2021-08-31
2. Research on the Standardization Measures of Unmanned Vehicle Security and Safety Evaluation and Verification
<br/>Title in Korean: 무인이동체 보안성·안전성 평가 및 검증 표준화 방안 연구
<br/>Sponsoring Auyhority: National Security Research Institute (국가보안기술연구소)
<br/>Duration: 2021-04-01 – 2021-10-31
3. Research Laboratory of RAS Assurance for Context-Aware Cluster Collaboration Embedded SW
<br/>Title in Korean:  상황인지 기반 군집협업형 임베디드 SW의 RAS 보증 연구실 (NRF 기초연구실 – 참여기관)
<br/>Sponsoring Authority: National Research Foundation of Korea (NRF, 한국연구재단)
<br/>Duration: 2021-03-01 – 2021-08-31
4. Research on Copyright Technology Trends and Technology Roadmap
<br/>Title in Korean: 저작권 기술 동향조사 및 기술로드맵 마련
<br/>Sponsoring Authority: Korea Copyright Commission (한국저작권위원회)
<br/>Duration: 2020-09-21 – 2020-12-15
5. Development of a Fuzzer-based Crash Management Interface for Collecting Executable File Information
<br/>Title in Korean: 실행 파일 정보 수집을 위한 퍼저 기반 크래시 관리 인터페이스 개발
<br/>Sponsoring Authority:  Electronics and Telecommunications Research Institute (ETRI, 한국전자통신연구원)
<br/>Duration: 2020-05-25 – 2020-09-24
6. Research and Development of Firmware Update Architecture in Private Blockchain Environment
<br/>Title in Korean: 사설 블록체인 환경에서의 펌웨어 업데이트 아키텍처 연구 및 개발
<br/>Sponsoring Authority: Electronics and Telecommunications Research Institute (ETRI, 한국전자통신연구원)
<br/>Duration: 2020-04-01 – 2020-10-31
7. Research on a Consensus Algorithm in a Public Blockchain Environment
<br/>Title in Korean: 공개형 블록체인 환경에서의 합의 알고리즘 연구
<br/>Sponsoring Authority: Electronics and Telecommunications Research Institute (ETRI, 한국전자통신연구원)
<br/>Duration: 2019-03-01 – 2019-11-30
8. Research on a Reliable Data Sharing System Based on Expendable Permissioned Blockchain
<br/>Title in Korean: 확장 가능한 허가형 블록체인 기반 신뢰 데이터 공유 체계 연구
<br/>Sponsoring Authority: Korea Institute of Science and Technology Information (한국과학기술정보연구원)
<br/>Duration: 2019-03-01 – 2019-08-31
9. Research onSignatureless blockchain platform and algorithm
<br/>Title in Korean: Signatureless 블록체인 플랫폼 및 알고리즘 연구
<br/>Sponsoring Authority: Electronics and Telecommunications Research Institute (ETRI, 한국전자통신연구원)
<br/>Duration: 2018-07-20 – 2018-11-30
10. Development of Blockchain Business Service Technology and Human Resources
<br/>Title in Korean: 블록체인 비즈니스 서비스 기술 개발 및 인력양성 (IITP ITRC – 참여기관)
<br/>Sponsoring Authority: Institute for Information & Communications Technology Promotion (IITP, 정보통신기술진흥센터)
<br/>Duration: 2018-07-01 – 2023-12-31
11. Research Laboratory of RAS Assurance for Distributed Embedded Systems Software
<br/>Title in Korean: 분산 임베디드 소프트웨어 RAS 보증 연구실 (NRF 기초연구실 – 참여기관)
<br/>Sponsoring Authority: National Research Foundation of Korea (NRF, 한국연구재단)
<br/>Duration: 2018-06-01 – 2021-02-28
12. Development of a Reliable Data Sharing System Based on Blockchains
<br/>Title in Korean: 블록체인 기반 신뢰 데이터 공유 시스템 개발
<br/>Sponsoring Authority: Korea Institute of Science and Technology Information (한국과학기술정보연구원)
<br/>Duration: 2018-05-01 – 2018-10-31
13. Development of Blockchain Based Digital Contents DRM Application Technology
<br/>Title in Korean: 블록체인 기반 디지털 콘텐츠 DRM 응용 기술 개발 (본 연구)
<br/>Sponsoring Authority: Korea Copyright Commission (한국저작권위원회)
<br/>Duration: 2018-01-01 – 2018-12-31
14. Development of Blockchain Based Digital Contents DRM Application Technology
<br/>Title in Korean: 블록체인 기반 디지털 콘텐츠 DRM 응용 기술 개발
<br/>Sponsoring Authority: Korea Copyright Commission (한국저작권위원회)
<br/>Duration: 2017-08-01 – 2017-11-30
15. Research on Requirement Analysis of Blockchain as a Service
<br/>Title in Korean: 클라우드에서 블록체인 서비스(Blockchain as a Service) 제공 분석 및 요구사항 개발
<br/>Sponsoring Authority: Electronics and Telecommunications Research Institute (ETRI, 한국전자통신연구원)
<br/>Duration: 2017-07-17 – 2017-11-30
16. Research on Security Guidelines for ICS Wireless Equipment Deployment and Usage
<br/>Title in Korean: 기반시설 무선장비 도입 및 활용 보안 가이드라인 연구
<br/>Sponsoring Authority: National Security Research Institute (국가보안기술연구소)
<br/>Duration: 2017-04-01 – 2017-10-31
17. Development of Mobile Edge Computing Platform Technology for URLLC Services
<br/>Title in Korean: 저지연 융합서비스를 위한 모바일 에지 컴퓨팅 플랫폼 기술 개발
<br/>Sponsoring Authority: Giga KOREA (기가코리아사업단)
<br/>Duration: 2017-04-01 – 2020-12-31
18. Study on Analysis of Security Requirements, Related Patents, and Standards for Vehicles
<br/>Title in Korean: 차량용 보안 요구사항 분석 및 관련 특허/표준화에 관한 연구
<br/>Sponsoring Authority: XXX (Private Firm)
<br/>Duration: 2017-02-15 – 2017-06-14
19. Development of Comparative Analysis Techniques and Verification Codes for Software and Source Codes
<br/>Title in Korean: 소프트웨어 및 소스코드 비교분석 기법 및 검증코드 개발
<br/>Sponsoring Authority: Supreme Prosecutors’ Office (대검찰청)
<br/>Duration: 2016-06-01 – 2016-12-28
</div>
</details>  
<br/>
  
### 🔧 Stack
* Golang
	+  Docker
	+ Kubernetes
* JavaScript
* PHP
* C
* Linux
<br/>
### 🏆 Prize  
* 2018 상명대학교 교내 프라임 경진대회 - __최우수상__
* 2017 KUCIS 우수 동아리 시상 - __최우수상__
* 2017 한국정보보호학회 하계 학술발표회 - __우수논문상__
<br/>
### 📄 Certificate
* Toeic Speaking Level 6 [click😊](./contents/3.pdf)
<br/>

### 📝 Blog
[ojo_96님의 블로그](https://blog.naver.com/ojo_96)
개발/일상 등을 올리는 **블로그**입니다.


[PEL(Protocol Engineering lab)]: http://pel.sejong.ac.kr/wordpress/
[Zeppelin]: https://zeppelin.apache.org/
[Clair]: https://www.redhat.com/en/topics/containers/what-is-clair 
