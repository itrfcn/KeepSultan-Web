#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: KeepSultan Flask Web
About: 基于KeepSultan项目的Flask网页版本
Author: LynxFrost


flask 应用入口文件
"""

from flask import Flask, render_template, request, jsonify, send_file
import os
import json
import io
from PIL import Image

# 导入KeepSultan的核心功能
from KeepSultan import KeepConfig, KeepSultanApp, AssetLoader
from KeepSultan import NumberRange, TimeRange, _ensure_time_str_hms

# 创建Flask应用
app = Flask(__name__)

# 主页路由
@app.route('/')
def index():
    return render_template('index.html')

# 生成图片的API路由
@app.route('/generate', methods=['POST'])
def generate_image():
    try:
        # 从表单获取配置数据
        config_data = request.form.to_dict()
        
        # 创建默认配置
        cfg = KeepConfig.from_json('config.json')
        
        # 处理基本参数
        if 'username' in config_data and config_data['username']:
            cfg.username = config_data['username']
        
        if 'date' in config_data and config_data['date']:
            cfg.date = config_data['date']
        
        if 'end_time' in config_data and config_data['end_time']:
            cfg.end_time = config_data['end_time']
        
        if 'location' in config_data and config_data['location']:
            cfg.location = config_data['location']
        
        if 'weather' in config_data and config_data['weather']:
            cfg.weather = config_data['weather']
        
        if 'temperature' in config_data and config_data['temperature']:
            cfg.temperature = config_data['temperature']
        
        # 处理base64编码的图片
        base64_fields = {
            'template_base64': 'template',
            'map_base64': 'map',
            'avatar_base64': 'avatar',
            'map_bg_base64': 'map_bg_path',
            'map_mask_base64': 'map_mask_path'
        }
        
        for base64_key, config_key in base64_fields.items():
            if base64_key in config_data and config_data[base64_key]:
                # 直接将base64编码的图片数据存储到配置中
                setattr(cfg, config_key, config_data[base64_key])
        
        # 处理数值范围参数
        range_params = ['total_km', 'cumulative_climb', 'average_cadence', 'exercise_load']
        for param in range_params:
            if f'{param}_low' in config_data and f'{param}_high' in config_data:
                try:
                    low = float(config_data[f'{param}_low'])
                    high = float(config_data[f'{param}_high'])
                    precision = 2 if param == 'total_km' else 0
                    setattr(cfg, param, NumberRange(low, high, precision))
                except ValueError:
                    pass
        
        # 处理时间范围参数
        time_params = ['sport_time', 'total_time']
        for param in time_params:
            if f'{param}_start' in config_data and f'{param}_end' in config_data:
                try:
                    start = config_data[f'{param}_start']
                    end = config_data[f'{param}_end']
                    setattr(cfg, param, TimeRange(start, end))
                except ValueError:
                    pass
        
        # 处理轨迹生成参数
        track_params = ['track_thickness', 'track_sample_rate', 'track_max_steps', 'track_target_length']
        for param in track_params:
            if param in config_data and config_data[param]:
                try:
                    setattr(cfg, param, int(config_data[param]))
                except ValueError:
                    pass
        
        if 'track_completion_threshold' in config_data and config_data['track_completion_threshold']:
            try:
                cfg.track_completion_threshold = float(config_data['track_completion_threshold'])
            except ValueError:
                pass
        
        # 处理轨迹颜色
        track_color = []
        for channel in ['b', 'g', 'r']:
            key = f'track_color_{channel}'
            if key in config_data and config_data[key]:
                try:
                    track_color.append(int(config_data[key]))
                except ValueError:
                    track_color.append(0)
            else:
                track_color.append(0)
        
        if len(track_color) == 3:
            cfg.track_color = tuple(track_color)
        
        # 创建应用实例并生成图片
        app_instance = KeepSultanApp(cfg)
        img = app_instance.process()
        
        # 将图片转换为字节流
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)
        
        # 生成以日期为名称的文件名
        from datetime import datetime
        if cfg.date == "today":
            date_str = datetime.now().strftime("%Y/%m/%d")
        else:
            date_str = cfg.date
        
        # 将日期格式化为适合文件名的格式（替换/为-）
        filename_date = date_str.replace("/", "-")
        download_filename = f'keep_{filename_date}.png'
        
        # 返回图片
        return send_file(img_byte_arr, mimetype='image/png', as_attachment=True, download_name=download_filename)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
