# Simple KAIST Menu-Bot

카이스트 문지캠퍼스의 오늘의 메뉴를 웹 스크래핑 하여 전송해 주는 슬랙 봇 입니다.

## Background

매 번 식단 확인을 위해 웹사이트에 접속해야 하는 9기 정글러들을 위해 간단히 제작해봤습니다.

## Tested Environments

- Ubuntu 24.04 LTS
- Python 3.12.5
- Firefox 129.0.2

## Setup

### Install firefox

Ubuntu 환경 내에서 firefox 를 설치하는 스크립트 입니다.

```bash
./install_firefox.sh
```

### Install dependencies

venv 환경 생성 및 필요한 라이브러리를 설치하는 스크립트 입니다.

```bash
./init.sh
```

### Copy env

```bash
cp .env.example .env
```

### Set value ​​in .env

채널에 통합된 슬랙 봇의 WEBHOOK_URL을 입력합니다.

```plaintext
WEBHOOK_URL="..."
```

## Run

venv 환경 activate 및 main.py 실행을 위한 스크립트 입니다.

### 아침 메뉴 전송

```bash
./run.sh breakfast
```

### 점심 메뉴 전송

```bash
./run.sh lunch
```

### 저녁 메뉴 전송

```bash
./run.sh dinner
```

## Automate it regularly

위의 방법은 1회 실행 후 종료되므로, 이를 주기적으로 실행하기 위해 ubuntu 내에서 crontab 을 이용할 수 있습니다.

`crontab -e` 을 실행한 뒤, 아래와 같이 작성할 수 있습니다.

```bash
0 22 * * * .../run.sh breakfast
0 02 * * * .../run.sh lunch
0 08 * * * .../run.sh dinner
```

각각 UTC 로 매일 22시, 02시, 08시에 아침, 점심, 저녁 메뉴를 전송한다는 의미입니다.

KST로 변환하면 07시, 11시, 17시가 됩니다.

이는 서버의 기본 타임존에 맞게 설정해야 합니다.

## Result with a Image

![image](https://github.com/user-attachments/assets/3f6747a7-e995-4a9d-9089-7488fc42bea4)

## Contributing

기여는 언제나 환영합니다!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
