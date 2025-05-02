# Dockerfile


#####20250430

FROM pytorch/pytorch:2.4.1-cuda12.4-cudnn9-devel

WORKDIR /app

COPY . .


RUN pip install flask
RUN pip install --no-cache-dir packaging
RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install --no-cache-dir flash-attn    # 이제 nvcc가 있으니 빌드 가능
RUN pip install --no-binary :all: flash-attn --verbose \
      --config-settings="--set=cmake.define.TORCH_CUDA_ARCH_LIST=7.5"

RUN pip install --no-cache-dir flask


ENV PYTHONPATH=/app/xcodec_mini_infer:$PYTHONPATH

EXPOSE 8080

CMD ["python", "app.py"]

##############################

