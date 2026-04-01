# KeepSultan-Web

KeepSultan-Web 是基于[KeepSultan](https://github.com/Carzit/KeepSultan)开发的网页版工具。

## 在线演示

[KeepSultan-Web 在线演示](https://k1.686909.xyz/)
无需安装，直接在浏览器中打开即可。

## 功能特点

- 📝 **基本信息自定义**：支持设置用户名、地点、日期、时间、天气、温度等信息
- 🎨 **运动数据配置**：可自定义总公里数、运动时间、总时间、累计爬升、平均步频、运动负荷等指标范围
- 🗺️ **轨迹生成设置**：支持调整轨迹颜色、厚度、采样率等参数
- 🖼️ **图片上传功能**：支持上传自定义模板、地图、头像等图片
- 💾 **本地数据缓存**：所有配置会自动保存到浏览器本地存储，刷新页面后无需重新设置
- 📁 **无服务器图片处理**：上传的图片采用base64编码存储在本地，不会上传到服务器
- 📦 **轻量级部署**：基于Flask框架，部署简单，占用资源少

## 技术栈

- **前端**：HTML、CSS、JavaScript
- **后端**：Python、Flask
- **图片处理**：Pillow、OpenCV
- **数据处理**：NumPy、SciPy
- **依赖管理**：uv、pip

## 安装步骤

### 1. 克隆项目

```bash
git clone https://github.com/itrfcn/KeepSultan-Web.git
cd KeepSultan-Web
```

### 2. 安装依赖

#### 使用uv（推荐）

```bash
uv sync
```

#### 使用pip

```bash
pip install -r requirements.txt
```

### 3. 运行项目

```bash
python main.py
```

项目将在 `http://127.0.0.1:5000` 运行

## 使用方法

1. **访问网页**：在浏览器中打开 `http://127.0.0.1:5000`

2. **填写基本信息**：
   - 用户名：输入您的用户名
   - 地点：输入运动地点
   - 日期：选择运动日期，默认为今天
   - 时间：选择运动结束时间，默认为当前时间
   - 天气：输入天气情况
   - 温度：输入温度

3. **配置运动数据范围**：
   - 设置总公里数、运动时间、总时间等指标的范围
   - 系统会在范围内随机生成具体数值

4. **调整轨迹生成配置**：
   - 选择轨迹颜色
   - 调整轨迹厚度
   - 设置采样率和目标路径长度

5. **上传自定义图片**（可选）：
   - 上传自定义模板、地图、头像等图片
   - 图片会转换为base64编码存储在本地

6. **生成图片**：
   - 点击"生成图片"按钮
   - 等待图片生成完成
   - 下载生成的图片

## 项目结构

```
KeepSultan-Web/
├── main.py              # Flask应用入口文件
├── KeepSultan.py        # 核心功能实现
├── pyproject.toml       # 项目配置和依赖
├── requirements.txt     # 依赖列表
├── config.json          # 配置文件
├── map.py               # 地图处理模块
├── fonts/               # 字体文件
│   ├── QanelasBlack.otf
│   ├── QanelasSemiBold.otf
│   └── SourceHanSansCN-Regular.otf
├── templates/           # HTML模板
│   └── index.html       # 主页面
├── src/                 # 资源文件
│   ├── template.png     # 默认模板图片
│   ├── map.png          # 默认地图图片
│   ├── avatar.png       # 默认头像图片
│   ├── map1.png         # 默认地图背景
│   ├── map2.png         # 默认路径掩码
│   ├── end.png          # 结束标记图片
│   ├── start.png        # 开始标记图片
│   └── map/             # 地图资源目录
│       └── map.png
├── .gitignore           # Git忽略文件
├── .python-version      # Python版本文件
└── uv.lock              # uv依赖锁定文件
```

## 注意事项

1. **本项目仅供学习交流使用，请勿用于商业用途**
2. **所有生成的图片数据仅保存在本地浏览器中，不会上传到服务器**
3. **支持上传自定义图片，图片会转换为base64编码存储在本地**
4. **网站会自动保存您的配置，刷新页面后无需重新设置**
5. **生成的图片文件名将包含日期信息，格式为：keep_YYYY-MM-DD.png**

## 鸣谢

- [KeepSultan](https://github.com/Carzit/KeepSultan)：本项目基于KeepSultan开发，感谢其核心功能实现。


## 贡献

- **贡献代码**：欢迎提交Pull Request，或在GitHub上报告问题
- **报告问题**：在项目仓库的Issues页面提交问题报告
- **参与讨论**：在项目仓库的Discussions页面参与讨论，分享您的经验或建议

## 许可证

MIT License

## 更新日志

### v0.1.0 (2026-04-01)
- 初始版本发布
- 实现基本的截图生成功能
- 支持用户自定义信息和配置
- 实现本地数据缓存
- 支持base64图片处理
