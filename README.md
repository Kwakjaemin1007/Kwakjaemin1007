<div align="center">

<img src="https://capsule-render.vercel.app/api?type=wave&color=0:0f2027,50:203a43,100:2c5364&height=220&section=header&text=Jaemin%20Kwak&fontColor=ffffff&fontSize=60&fontAlignY=30&desc=Cloud%20%C2%B7%20Network%20%C2%B7%20DevOps&descAlignY=47&descSize=20" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Noto+Sans+KR&weight=500&size=18&duration=3500&pause=800&color=2C5364&center=true&vCenter=true&width=520&lines=%EC%84%9C%EB%B9%84%EC%8A%A4%EB%A5%BC+%EC%95%88%EC%A0%95%EC%A0%81%EC%9C%BC%EB%A1%9C+%EB%B0%B0%ED%8F%AC%ED%95%98%EA%B3%A0+%EC%9A%B4%EC%98%81%ED%95%98%EB%8A%94+%EC%97%94%EC%A7%80%EB%8B%88%EC%96%B4;Konkuk+Univ.+Computer+Science+%2F+3rd+year;Now+designing%3A+5G+Core+on+Kubernetes" alt="typing"/>

</div>

<br>

## About

건국대학교 컴퓨터공학부 3학년입니다. 클라우드 인프라와 네트워크를 중심으로, 서비스를 설계부터 배포·운영까지 끝까지 책임지는 엔지니어를 목표로 하고 있습니다.

- 🛰️ **Now** · Kubernetes 위에 오픈소스 5G 코어를 올려 배포·운영하는 **CoreOps** 프로젝트 설계 중
- 📚 **Studying** · AWS SAA → CCNA, Terraform, Kubernetes
- 🧩 **Done before** · FastAPI 비동기 백엔드(S3·Redis 큐), 컴퓨터 비전 모델 학습·추론, Android 앱, C로 OS 메모리 관리 구현

<br>

## Tech Stack

<table>
  <tr>
    <td align="center" width="140"><b>Cloud · Infra</b></td>
    <td><img src="https://skillicons.dev/icons?i=aws,linux,git,githubactions&perline=10" height="40"/></td>
  </tr>
  <tr>
    <td align="center"><b>Backend</b></td>
    <td><img src="https://skillicons.dev/icons?i=python,fastapi,postgres,redis&perline=10" height="40"/></td>
  </tr>
  <tr>
    <td align="center"><b>Mobile · AI</b></td>
    <td><img src="https://skillicons.dev/icons?i=kotlin,androidstudio,firebase,pytorch,opencv&perline=10" height="40"/></td>
  </tr>
  <tr>
    <td align="center"><b>Systems</b></td>
    <td><img src="https://skillicons.dev/icons?i=c&perline=10" height="40"/></td>
  </tr>
  <tr>
    <td align="center"><b>Learning</b></td>
    <td><img src="https://skillicons.dev/icons?i=docker,kubernetes,terraform&perline=10" height="40"/></td>
  </tr>
</table>

<br>

## Featured Projects

### 🛡️ DDP — 딥페이크 탐지 플랫폼

[![repo](https://img.shields.io/badge/AICV--Deepfaker-deepfaker__detection-181717?style=flat-square&logo=github)](https://github.com/AICV-Deepfaker/deepfaker_detection)
![](https://img.shields.io/badge/멋쟁이사자처럼_CV_부트캠프-최종_프로젝트-2c5364?style=flat-square)
![](https://img.shields.io/badge/2026.01~02-gray?style=flat-square)

영상이나 YouTube 링크를 넣으면 주파수·심박(rPPG)·음성 분석으로 딥페이크 여부를 판정하는 서비스.
FastAPI가 요청을 받고 Taskiq + Redis 큐로 넘겨 워커가 비동기로 분석합니다.

| 맡은 일 | 내용 |
|---|---|
| 🗂️ 백엔드 설계 | 요구사항 ID 기준으로 회원·미디어·챗봇 3개 파트 역할 분담표 작성 |
| ☁️ 업로드 파이프라인 | 영상 업로드·URL 입력 → S3 저장 → 비동기 분석 → 결과 저장·알림 API ([#3](https://github.com/AICV-Deepfaker/deepfaker_detection/pull/3)) |
| 🧹 스토리지 관리 | 회원 탈퇴 시 S3 프로필·영상 일괄 삭제, 중복 S3 삭제 함수 통합 |
| ❤️ rPPG 모델 | EfficientPhys(rPPG-Toolbox) 추가 학습, 전처리·탐지기 백엔드 연동, 신호 시각화 ([#4](https://github.com/AICV-Deepfaker/deepfaker_detection/pull/4)–[#6](https://github.com/AICV-Deepfaker/deepfaker_detection/pull/6)) |

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![AWS S3](https://img.shields.io/badge/AWS_S3-569A31?style=flat-square)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)

<br>

<table>
<tr>
<td width="50%" valign="top">

#### 🍓 [딸기 병해 진단](https://github.com/Kwakjaemin1007/Like-lion_-Smart-farm)
`멋사 CV 부트캠프` `2026.01 · 7일 · 4명`

YOLO로 잎·과실을 찾고 EfficientNet-B0로 5종 분류하는 2단계 파이프라인.
**분류 Test 정확도 83.5%**

내 역할: YOLO v5·v8·11 비교, 증강·클래스 축소·해상도 실험, 탐지→분류 파이프라인 구축

</td>
<td width="50%" valign="top">

#### 🛣️ 차선 감지 모델 비교
`멋사 CV 부트캠프` `2026.01`

차선 인식 모델들을 팀원별로 맡아 비교.
**내가 맡은 모델이 팀 최종 모델로 선정**

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### 📈 [EconUp](https://github.com/Kwakjaemin1007/EconUp)
`개인 프로젝트` `2026.05`

플래시카드와 퀴즈로 하루 10분씩 경제용어를 익히는 Android 앱. AI 코딩 도구 활용.

`Kotlin` `Compose` `Room` `Retrofit` `Firestore`

</td>
<td width="50%" valign="top">

#### 🗑️ [쓰레기 감지 카메라](https://github.com/Kwakjaemin1007/2-2-Iot)
`세종대 IoT 학술제` `2023`

YOLOv5로 쓰레기를 탐지하는 카메라 기기 아이디어 구현.
아이디어 구상, 모델 선정·학습 담당.

`YOLOv5` `Python`

</td>
</tr>
</table>

<br>

## 🛰️ Now Building — CoreOps

AWS 위 Kubernetes에 오픈소스 5G 코어(Open5GS)와 기지국·단말 시뮬레이터(UERANSIM)를 올려 "작은 통신사"를 만들고, IaC·GitOps로 배포하며 망 품질 지표로 이상을 탐지하는 프로젝트입니다.

```
UE x N --- gNB --N2 (NGAP)--> AMF / SMF / NRF / UDM
               `-N3 (GTP-U)-> UPF --N6--> Internet / MEC

Terraform (VPC, k3s) -> GitHub Actions (E2E test) -> Argo CD -> Prometheus / Grafana
```

- [ ] 0단계 · 요구사항 · 아키텍처 · IP 계획 · 시퀀스 다이어그램 설계
- [ ] 1단계 · docker compose로 5G 코어 로컬 구동, 패킷 캡처 분석
- [ ] 2단계 · Terraform으로 AWS VPC · k3s 구축
- [ ] 3단계 · Helm · Argo CD · GitHub Actions
- [ ] 4~6단계 · 네트워크 슬라이싱 · MEC · 관측성 · 장애 실험

<br>

## Education & Certifications

| | |
|---|---|
| 🎓 | **건국대학교** 컴퓨터공학부 (편입, 재학) · **세종대학교** 소프트웨어학과 (편입 전) |
| 🦁 | **멋쟁이사자처럼 CV 부트캠프** · 2025.12 ~ 2026.02 — CNN·Transformer 이론, 탐지·분할·생성 모델 실습, 팀 프로젝트 3건 |
| ☁️ | **AWS Certified Cloud Practitioner** (CLF-C02) |

<br>

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=wave&color=0:2c5364,50:203a43,100:0f2027&height=110&section=footer" width="100%"/>
</div>
