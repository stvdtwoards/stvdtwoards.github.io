import os
import imageio

# 原始视频文件夹
input_dir = r"I:\github.io-master\github.io-master\static\videos\need"
# 目标存储文件夹
output_dir = r"I:\github.io-master\github.io-master\static\videos\need_o"

# 确保目标文件夹存在
os.makedirs(output_dir, exist_ok=True)

# 遍历目录下的所有视频文件
for filename in os.listdir(input_dir):
    if filename.lower().endswith((".mp4", ".avi", ".mov", ".mkv")):  # 仅处理特定格式的视频
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)  # 目标文件路径

        print(f"正在处理: {filename}")

        try:
            # 读取视频
            reader = imageio.get_reader(input_path)
            fps = reader.get_meta_data().get("fps", 30)  # 获取帧率，默认30

            # 创建视频写入对象
            writer = imageio.get_writer(output_path, fps=fps)

            # 逐帧写入
            for frame in reader:
                writer.append_data(frame)

            # 释放资源
            reader.close()
            writer.close()

            print(f"已完成: {filename}")

        except Exception as e:
            print(f"处理 {filename} 失败: {e}")

print("所有视频处理完成！")
