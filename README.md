 # Telegram 反登录机器人

## 项目简介

这是一个基于Telethon库开发的Telegram防登录功能，主要功能是监控Telegram官方账户(777000)发送的登录通知消息，并将这些消息自动转发到指定的机器人账户使登录代码失效，帮助用户实时监控账户登录活动，提高账户安全性。

还可以用于+888反登录保护
可以禁止租售方注销888登录
一经登录888账户，即可长期持有
以及其他多种反登录需求！

### Bot免费托管
Bot托管，功能定制，自由组合！
免费提供多种常用功能：双向聊天客服，频道/群组管理！
界面管理.人性化操作，简单易用！

免费体验：[@FriesOfficialBot](https://t.me/FriesOfficialBot)
技术讨论：[https://t.me/FriesClub](https://t.me/FriesClub)

## 功能特点

1. **防登录监控**：监控Telegram官方账户发送的登录通知消息
2. **自动转发**：将登录通知自动转发到指定的机器人账户使验证码失效
3. **命令控制**：通过简单的文本命令开启/关闭防登录功能
4. **状态查询**：随时查询防登录功能的开启状态
5. **多账户支持**：支持同时管理多个Telegram账户

## 工作原理

1. 程序使用Telethon库连接Telegram API
2. 监听来自Telegram官方账户(777000)的消息
3. 当防登录功能开启时，自动将这些消息转发到指定的机器人账户
4. 用户可以通过发送命令控制防登录功能的开启和关闭



## 命令列表

- `self check` - 测试机器人是否正常工作
- `antilogin` - 查询防登录功能的当前状态
- `antilogin on` - 开启防登录功能
- `antilogin off` - 关闭防登录功能

## 使用前准备

1. 获取Telegram API凭证：
   - API_ID
   - API_HASH
   - BOT_TOKEN (如果需要作为机器人运行)

2. 设置转发目标：
   - 修改`FORWARD_BOT_USERNAME`为您想要接收转发消息的机器人用户名

## 安装依赖

```bash
pip install telethon asyncio
```

## 配置说明

在使用前，请修改代码中的以下配置项：

```python
# API凭证
API_ID = None  # 替换为您的API ID
API_HASH = ''  # 替换为您的API哈希
BOT_TOKEN = ''  # 替换为您的机器人令牌
FORWARD_BOT_USERNAME = '@FriesOfficialBot'  # 设置转发消息的目标机器人用户名
```

## 运行方法

```bash
python bot.py
```

## 安全提示

1. 请勿将您的API凭证泄露给他人
2. 定期检查您的活跃会话
3. 开启两步验证以提高账户安全性

## 技术架构

- **Telethon库**：用于与Telegram API交互
- **异步编程**：使用asyncio处理异步操作，提高效率
- **事件监听**：通过事件处理器监听特定类型的消息

## 注意事项

- 本程序仅用于个人账户安全保护，请勿用于非法用途
- 使用本程序时请遵守Telegram的服务条款
- 过度频繁的API调用可能导致账户被限制
