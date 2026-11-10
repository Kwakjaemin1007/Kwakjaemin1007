<!-- 이 파일은 scripts/build_readme.py가 profile.yml로 자동 생성합니다. 직접 수정하지 마세요. -->

<div align="center">

# 곽재민 · Jaemin Kwak

**Cloud · Network · DevOps**  
건국대학교 컴퓨터공학부 3학년

<img src="https://img.shields.io/badge/Location-Seoul-2c5364?style=flat-square" alt="Location"/> <img src="https://img.shields.io/badge/Focus-Cloud_%C2%B7_Network_%C2%B7_DevOps-2c5364?style=flat-square" alt="Focus"/>

</div>

## About

클라우드 인프라와 네트워크를 중심으로, 서비스를 설계부터 배포·운영까지 책임지는 엔지니어를 목표로 하고 있습니다.

- **CoreOps** — Kubernetes 위에 오픈소스 5G 코어를 올려 배포·운영하는 프로젝트 설계 중
- AWS Solutions Architect Associate → CCNA 준비

## Tech Stack

| | |
|:--|:--|
| **Cloud · Infra** | <img src="https://skillicons.dev/icons?i=aws,linux,git,githubactions" height="36"/> |
| **Backend** | <img src="https://skillicons.dev/icons?i=python,fastapi,postgres,redis" height="36"/> |
| **Mobile · AI** | <img src="https://skillicons.dev/icons?i=kotlin,androidstudio,firebase,pytorch,opencv" height="36"/> |
| **Systems** | <img src="https://skillicons.dev/icons?i=c" height="36"/> |
| **Learning** | <img src="https://skillicons.dev/icons?i=docker,kubernetes,terraform" height="36"/> |

## Featured

### [DDP — 딥페이크 탐지 플랫폼](https://github.com/AICV-Deepfaker/deepfaker_detection)

<sub>멋쟁이사자처럼 CV 부트캠프 최종 프로젝트 · 2026.01 – 02</sub>

영상이나 YouTube 링크를 넣으면 주파수·심박(rPPG)·음성 분석으로 딥페이크 여부를 판정하는 서비스. FastAPI가 요청을 받고 Taskiq + Redis 큐로 넘겨 워커가 비동기로 분석합니다.

| 맡은 일 | 내용 |
|:--|:--|
| 백엔드 설계 | 요구사항 ID 기준으로 회원·미디어·챗봇 3개 파트 역할 분담표 작성 |
| 업로드 파이프라인 | 영상 업로드·URL 입력 → S3 저장 → 비동기 분석 → 결과 저장·알림 API [#3](https://github.com/AICV-Deepfaker/deepfaker_detection/pull/3) |
| 스토리지 관리 | 회원 탈퇴 시 S3 프로필·영상 일괄 삭제, 중복 S3 삭제 함수 통합 |
| rPPG 모델 | EfficientPhys(rPPG-Toolbox) 추가 학습, 전처리·탐지기 백엔드 연동, 신호 시각화 [#4](https://github.com/AICV-Deepfaker/deepfaker_detection/pull/4), [#5](https://github.com/AICV-Deepfaker/deepfaker_detection/pull/5), [#6](https://github.com/AICV-Deepfaker/deepfaker_detection/pull/6) |

`FastAPI` `Taskiq` `Redis` `AWS S3` `PostgreSQL` `PyTorch`

## Projects

| 프로젝트 | 내용 | 역할 | 기술 |
|:--|:--|:--|:--|
| **[딸기 병해 진단](https://github.com/Kwakjaemin1007/Like-lion_-Smart-farm)**<br><sub>멋사 CV 부트캠프 · 2026.01 · 4명</sub> | YOLO 탐지 → EfficientNet-B0 5종 분류 2단계 파이프라인, 분류 Test 정확도 83.5% | YOLO v5·v8·11 비교, 증강·클래스 축소·해상도 실험, 파이프라인 구축 | `PyTorch` `YOLO` `EfficientNet` |
| **차선 감지 모델 비교**<br><sub>멋사 CV 부트캠프 · 2026.01</sub> | 차선 인식 모델들을 팀원별로 맡아 성능 비교 | 담당 모델이 팀 최종 모델로 선정 | `PyTorch` |
| **[EconUp](https://github.com/Kwakjaemin1007/EconUp)**<br><sub>개인 · 2026.05</sub> | 플래시카드·퀴즈로 경제용어를 익히는 Android 앱 (AI 코딩 도구 활용) | 기획·구현 | `Kotlin` `Compose` `Room` `Firestore` |
| **[쓰레기 감지 카메라](https://github.com/Kwakjaemin1007/2-2-Iot)**<br><sub>세종대 IoT 학술제 · 2023</sub> | YOLOv5로 쓰레기를 탐지하는 카메라 기기 아이디어 구현 | 아이디어 구상, 모델 선정·학습 | `YOLOv5` `Python` |

## Now Building — CoreOps

AWS 위 Kubernetes에 오픈소스 5G 코어(Open5GS)와 기지국·단말 시뮬레이터(UERANSIM)를 올려 "작은 통신사"를 만들고, IaC·GitOps로 배포하며 망 품질 지표로 이상을 탐지합니다.

<img src="https://img.shields.io/badge/progress-0%2F7_%280%25%29-2c5364?style=flat-square" alt="progress"/>

- [ ] 0. 설계 — 요구사항 · 아키텍처 · IP 계획 · 시퀀스 다이어그램
- [ ] 1. docker compose로 5G 코어 로컬 구동, 패킷 캡처 분석
- [ ] 2. Terraform으로 AWS VPC · k3s 구축
- [ ] 3. Helm · Argo CD · GitHub Actions 배포 자동화
- [ ] 4. 네트워크 슬라이싱 · MEC 경로별 지연 비교
- [ ] 5. Prometheus · Grafana 관측성, 운영 API
- [ ] 6. 부하 · 장애 실험과 이상 탐지

## Education & Certifications

- **건국대학교** 컴퓨터공학부 (편입, 재학)
- **세종대학교** 소프트웨어학과 (편입 전)
- **멋쟁이사자처럼 CV 부트캠프** · 2025.12 – 2026.02 — 탐지·분할·생성 모델 실습, 팀 프로젝트 3건
- AWS Certified Cloud Practitioner (CLF-C02)
