# Lightweight-and-Efficient-YOLOv5

## Introduction
As the world accelerates towards **"Physical AI and Edge AI"**, the demand for deploying intelligent systems on edge devices (drones, mobile phones, IoT sensors) is exploding. These environments demand models that are not just accurate, but also **lightweight (small memory footprint)** and **efficient (fast inference)**.

This repository hosts a robust framework for building and exporting such models for **Multiple-Object-Detection** using the YOLO framework and **Post Training Quantization (PTQ)**.

The goal is simple: Create models that mirror the high accuracy of massive YOLO architectures while remaining small enough to run on constrained hardware.

---

## Datasets Implemented
We have benchmarked this framework on the **Rice Quality Dataset**:
* **Source:** [Roboflow Universe - Rice Quality 3](https://universe.roboflow.com/project-klj99/rice-quality-3)
* **Task:** Multi-class Object Detection
* **Classes (8):** `broken-chalky`, `broken-clear`, `foreign-object`, `plastic`, `sound`, `stone`, `unsound`, `whole-chalky`

### Model Selection
We selected the **YOLOv5 Nano** model for this task due to its:
1.  **Stability:** Proven architecture for object detection.
2.  **Quantizability:** Easier to quantize effectively compared to newer, more complex architectures.
3.  **Efficiency:** Native lightweight design suitable for edge deployment.

---

## Methodology Framework
Our pipeline ensures maximum efficiency without sacrificing predictive power:

1.  **Dataset Analysis:** Analyze class distribution and variances.
2.  **Model Selection:** Adopt YOLOv5 Nano.
3.  **Optimization Training:** Train the FP32 Nano model using optimal hyperparameters and augmentations to maximize baseline accuracy.
4.  **Export:** Convert the trained PyTorch model to **FP32 ONNX**.
5.  **Post Training Quantization (PTQ):** Convert the FP32 ONNX model to **INT8 ONNX** using static quantization.
6.  **Benchmarking:** Rigorous testing for accuracy (mAP), speed (latency), and efficiency (size).

---

## Results of Experiments

The experiments were conducted on **Google Colab (T4 GPU)**.

### 1. Accuracy & Performance Comparison
Despite the aggressive compression to INT8, the model retains nearly identical accuracy to the FP32 baseline.

| Metric | FP32 Baseline | INT8 Quantized | Change |
| :--- | :--- | :--- | :--- |
| **Precision (P)** | 0.834 | 0.855 | +2.5% |
| **Recall (R)** | 0.818 | 0.798 |  -2.4% |
| **mAP@50** | **0.885** | **0.885** | **0.0% (No Loss)** |
| **mAP@50-95** | 0.759 | 0.742 | -2.2% |

### 2. Efficiency Analysis (Size)
Quantization significantly reduced the model footprint, making it ideal for storage-constrained edge devices.

| Metric | FP32 ONNX | INT8 ONNX | Improvement |
| :--- | :--- | :--- | :--- |
| **Model Size** | 8.06 MB | **2.99 MB** | **~2.7x Smaller** |

### 3. Detailed Class-wise Performance (mAP@50)
The INT8 model maintains high precision across difficult classes like `plastic` and `stone`.

| Class | FP32 mAP@50 | INT8 mAP@50 |
| :--- | :--- | :--- |
| broken-chalky | 0.752 | 0.786  |
| broken-clear | 0.852 | 0.847 |
| foreign-object | 0.937 | 0.926  |
| plastic | 0.910 | 0.918  |
| sound | 0.925 | 0.917  |
| stone | 0.921 | 0.913  |
| unsound | 0.930 | 0.931  |
| whole-chalky | 0.857 | 0.840 |

*(Note: Inference speeds observed were 255.32ms for FP32 and 298.28ms for INT8 on the specific T4 GPU environment configuration used).*

---

## Repository Structure

* **`Mobile-App-Demo/`**
    Contains demo videos of a basic mobile app created to deploy these INT8 ONNX models directly on a physical device.
* **`Model_files/`**
    Stores the exported `.onnx` files (FP32 & INT8) and the model weights.
* **`Train-Notebooks/`**
    Complete Jupyter notebooks containing the code for the entire framework (Training, Exporting, Quantizing).
* **`predict.py`**
    A utility script to test the models on your own images.

---

## Conclusion
This framework provides a highly optimized pathway for developers and researchers pursuing **Physical AI and Edge AI**. By leveraging **Post-Training Quantization (PTQ)**, we demonstrate that massive hardware is not required to run intelligent visual recognition systems. We successfully deployed a high-accuracy **Multiple Object Detection** system (YOLOv5) with a minimal memory footprint.
