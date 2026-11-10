# 곽재민 · Jaemin Kwak

건국대학교 컴퓨터공학부 3학년입니다.
클라우드 인프라와 네트워크를 중심으로, 서비스를 안정적으로 배포하고 운영하는 엔지니어를 목표로 하고 있습니다.

- 지금 하는 것: AWS 아키텍처와 네트워크 공부
- 다음 목표: AWS SAA → CCNA, Kubernetes 위에 오픈소스 5G 코어를 올려 배포·운영하는 CoreOps 프로젝트 (설계 단계)
- 그동안 해 온 것: FastAPI 백엔드, Android(Kotlin) 앱, 컴퓨터 비전 모델 학습·추론, C로 OS 메모리 관리 구현

<br>

## Projects

### DDP — 딥페이크 탐지 플랫폼
[AICV-Deepfaker/deepfaker_detection](https://github.com/AICV-Deepfaker/deepfaker_detection) · 멋쟁이사자처럼 CV 부트캠프 최종 프로젝트 · 2026.01 ~ 02 (약 1개월)

영상이나 YouTube 링크를 넣으면 주파수·심박(rPPG)·음성 분석으로 딥페이크 여부를 판정하는 서비스입니다.
요청은 FastAPI가 받고, Taskiq + Redis 큐로 넘겨 워커가 비동기로 분석합니다.

내가 맡은 부분 (S3 스토리지 · 백엔드 · rPPG 모델)
- 요구사항 ID 기준으로 백엔드를 회원·미디어·챗봇 3개 파트로 나눈 역할 분담표 작성
- 영상 업로드·URL 입력 → S3 저장 → 비동기 분석 → 결과 저장·알림으로 이어지는 API 파이프라인 구현 ([#3](https://github.com/AICV-Deepfaker/deepfaker_detection/pull/3))
- 회원 탈퇴 시 S3에 남는 프로필·영상 파일을 함께 지우도록 삭제 로직 정리, 중복된 S3 삭제 함수 통합
- rPPG 논문 리뷰 후 EfficientPhys(rPPG-Toolbox) 추가 학습, 전처리·탐지기를 백엔드에 연결하고 신호 시각화 추가 ([#4](https://github.com/AICV-Deepfaker/deepfaker_detection/pull/4)–[#6](https://github.com/AICV-Deepfaker/deepfaker_detection/pull/6))

`FastAPI` `SQLModel` `Taskiq` `Redis` `AWS S3` `PyTorch`

### 딸기 병해 진단
[Like-lion_-Smart-farm](https://github.com/Kwakjaemin1007/Like-lion_-Smart-farm) · 멋쟁이사자처럼 CV 부트캠프 팀 프로젝트 · 2026.01 (7일) · 4명

YOLO로 잎·과실을 찾고, 잘라낸 영역을 EfficientNet-B0로 5종(정상 포함) 분류하는 2단계 파이프라인입니다.
분류 모델 Test 정확도 83.5% (클래스별 81장 균형 평가).

내가 맡은 부분: YOLO 탐지 모델 실험(v5·v8·11 비교, 증강·클래스 축소·해상도 실험)과 탐지→분류 2단계 파이프라인 구축

`PyTorch` `YOLO` `EfficientNet` `Google Colab`

### 차선 감지 모델 비교
멋쟁이사자처럼 CV 부트캠프 팀 프로젝트 · 2026.01

차선을 잘 인식하는 모델들을 팀원별로 맡아 비교했고, 제가 맡은 모델이 팀 최종 모델로 선정됐습니다.

### 쓰레기 감지 카메라
[2-2-Iot](https://github.com/Kwakjaemin1007/2-2-Iot) · 세종대 IoT 학술제 · 2023

YOLOv5로 쓰레기를 탐지하는 카메라 기기 아이디어를 구현한 프로젝트입니다.
아이디어 구상과 모델 선정·학습을 맡았습니다.

`YOLOv5` `Python`

### EconUp
[EconUp](https://github.com/Kwakjaemin1007/EconUp) · 개인 프로젝트 · 2026.05

플래시카드와 퀴즈로 하루 10분씩 경제용어를 익히는 Android 앱입니다. AI 코딩 도구를 활용해 구현했습니다.

`Kotlin` `Jetpack Compose` `Room` `Retrofit` `Firebase Firestore`

<br>

## Skills

| 분야 | 사용해 본 것 |
|---|---|
| Cloud | AWS (S3), Firebase |
| Backend | Python, FastAPI, SQLModel, Redis, Taskiq |
| Mobile | Kotlin, Jetpack Compose, Room |
| AI | PyTorch, YOLO, EfficientNet |
| Systems | C, Linux |
| 공부 중 | Docker, Terraform, Kubernetes, 네트워크(CCNA 범위) |

<br>

## Education & Training

- 건국대학교 컴퓨터공학부 (편입, 재학)
- 세종대학교 소프트웨어학과 (편입 전)
- 멋쟁이사자처럼 CV 부트캠프 · 2025.12 ~ 2026.02
  - CNN·RNN·Attention 이론(CS231n 스터디), YOLO 탐지·FCN/U-Net/DeepLabV3+ 분할·GAN 실습
  - 산불 연기 탐지 개선 실습: YOLOv5s 학습 설정 조정으로 Precision 0.811 → 0.921, mAP50-95 0.446 → 0.53
  - 팀 프로젝트 3건: 딸기 병해 진단(7일), 차선 감지 모델 비교, DDP 딥페이크 탐지 플랫폼(약 1개월)

<br>

## Certifications

- AWS Certified Cloud Practitioner (CLF-C02)
