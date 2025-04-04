import asyncio
from aiogram import Bot

# 토큰을 입력하세요
API_TOKEN = '7692394239:AAEp-_POjM7qaQ0qHaUbMuQ-KMs6_Ho5Pw8'
chat_id = '8135186841'

async def send_message(text):
    bot = Bot(token=API_TOKEN)
    await bot.send_message(chat_id=chat_id, text=text)
    await bot.close()

async def main():
    while True:
        # 사용자로부터 메시지를 입력받음
        message = input("보낼 메시지를 입력하세요 (종료하려면 'exit' 입력): ")
        if message.lower() == 'exit':
            print("메시지 전송을 종료합니다.")
            break

        # 메시지를 전송
        await send_message(message)

if __name__ == "__main__":
    asyncio.run(main())