import os
import subprocess

def download_twitch_vod(vod_url, output_filename, quality="best", threads=4, timeout=60, retries=3):
    try:
        command = [
            'streamlink', 
            vod_url, 
            quality, 
            '-o', output_filename, 
            f'--hls-segment-threads={threads}',
            f'--hls-segment-timeout={timeout}',
            f'--retry-streams={retries}'
        ]

        subprocess.run(command, check=True)
        print(f"Download completo: {output_filename}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao baixar o VOD: {e}")

if __name__ == "__main__":
    vod_url = input("Insira a URL do VOD da Twitch: ")
    output_filename = input("Insira o nome do arquivo de saída (ex: video.mp4): ")
    
    #region Configurações de qualidade e threads
    quality = input("Escolha a qualidade (ex: 720p, 480p, best): ") or "best"
    threads = input("Número de threads simultâneas (padrão 4, porém sinta-se livre para teste 8 ou 16): ")
    
    threads = int(threads) if threads.isdigit() else 4

    download_twitch_vod(vod_url, output_filename, quality, threads)
    #endregion