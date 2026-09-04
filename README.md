# AWS Linux CloudOps Lab

AWS와 Linux 환경에서 클라우드 서버를 직접 구축하고 운영하며,
Linux 서버 관리, 웹 서비스 배포, 컨테이너 운영 및 장애 대응을 학습하기 위한 개인 프로젝트입니다.

## 프로젝트 목표

- AWS EC2 기반 Ubuntu Linux 서버 구축
- SSH를 이용한 원격 서버 접속 및 관리
- Linux 기본 명령어와 시스템 관리 실습
- Nginx Reverse Proxy 구성
- Docker 기반 애플리케이션 실행환경 구축
- 서비스 장애 상황 재현 및 원인 분석
- 향후 AWS 네트워크, 모니터링, CI/CD, IaC까지 확장

## 현재 아키텍처

Internet  
↓ HTTP :80  
AWS Security Group  
↓  
EC2 (Ubuntu Linux)  
↓  
Nginx  
↓ Reverse Proxy  
127.0.0.1:8000  
↓ Port Mapping  
Docker Container  
↓  
Uvicorn  
↓  
FastAPI

## 현재 적용 기술

- AWS EC2
- Ubuntu Linux
- SSH
- Nginx
- Docker
- Python
- FastAPI
- Uvicorn

## 진행 상황

- [x] GitHub Repository 생성
- [x] AWS EC2 Ubuntu 인스턴스 생성
- [x] SSH 원격 접속
- [x] Linux 서버 기본 상태 확인
- [x] FastAPI 애플리케이션 구현 및 실행
- [x] Nginx Reverse Proxy 설정
- [x] Docker 설치
- [x] FastAPI Docker Image 빌드
- [x] Docker Container 실행
- [x] Nginx와 Docker Container 연동
- [x] Docker Container 장애 재현 및 복구
- [ ] VPC 및 Public / Private Subnet 구성
- [ ] RDS MySQL 연동
- [ ] Backup / Recovery 실습
- [ ] CloudWatch 모니터링
- [ ] GitHub Actions 기반 CI/CD
- [ ] Terraform 기반 IaC
- [ ] 프로젝트 최종 문서화

## 주요 구현 내용

### 1. AWS EC2 Linux 서버 구축

Ubuntu 기반 EC2 인스턴스를 생성하고 SSH Key Pair를 이용하여 원격 접속 환경을 구성했습니다.

Linux 서버에서 다음 명령어를 이용해 시스템 상태를 확인했습니다.

- `whoami`
- `hostname`
- `uname -a`
- `ip addr`
- `df -h`
- `free -h`
- `systemctl`

### 2. FastAPI 애플리케이션

서버의 CPU, Memory, Disk 등의 상태를 확인할 수 있는 간단한 FastAPI 애플리케이션을 구성했습니다.

초기에는 Python 가상환경에서 Uvicorn을 직접 실행했습니다.

### 3. Nginx Reverse Proxy

FastAPI의 8000번 포트를 인터넷에 직접 노출하지 않고,
Nginx가 HTTP 80번 포트로 요청을 받은 뒤 내부 FastAPI로 전달하도록 구성했습니다.

요청 흐름:

Internet  
→ Nginx :80  
→ 127.0.0.1:8000  
→ FastAPI

### 4. Docker 적용

기존 Python 가상환경 기반 실행 방식에서 Docker Container 기반 실행 방식으로 변경했습니다.

Dockerfile을 이용하여 애플리케이션 실행환경을 Image로 구성하고,
해당 Image를 기반으로 Container를 실행했습니다.

현재 구조:

Nginx  
→ EC2 127.0.0.1:8000  
→ Docker Container :8000  
→ Uvicorn  
→ FastAPI

## Troubleshooting

### Docker Container 중지로 인한 서비스 장애

#### 현상

FastAPI Container를 중지한 후 Nginx를 통한 서비스 요청이 정상적으로 처리되지 않았습니다.

#### 확인 과정

1. `curl`을 이용하여 HTTP 응답 확인
2. `systemctl status nginx`로 Nginx 상태 확인
3. `docker ps`로 실행 중인 Container 확인
4. `docker ps -a`로 종료된 Container 확인
5. `docker logs`로 Container 로그 확인

#### 원인

FastAPI가 실행 중이던 Docker Container가 중지되어
Nginx가 upstream 애플리케이션에 연결할 수 없었습니다.

#### 조치

Docker Container를 다시 시작한 후 `curl`을 통해 정상 응답을 확인했습니다.

## 향후 개선

- AWS VPC 및 Public / Private Subnet 설계
- RDS MySQL을 Private Subnet에 구성
- EBS / RDS Backup 및 Recovery 실습
- AWS CloudWatch 기반 모니터링
- GitHub Actions 기반 CI/CD
- Terraform을 이용한 Infrastructure as Code
