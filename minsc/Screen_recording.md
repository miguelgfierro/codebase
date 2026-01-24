# Screen recording

## OBS

### Installation

**Windows:**
1. Download OBS Studio from [obsproject.com](https://obsproject.com)
2. Run the installer and follow the prompts
3. Launch OBS and complete the auto-configuration wizard

**Alternative (winget):**
```bash
winget install OBSProject.OBSStudio
```

### 4K Recording Setup with NVIDIA DSR

To record in 4K on a laptop display, use NVIDIA's Deep Learning Super Resolution.

#### Step 1: Enable NVIDIA DSR

1. Right-click desktop → **NVIDIA Control Panel**
2. Go to **Manage 3D settings** → **Global Settings**
3. Find **DSR - Factors**
4. Check **2.25x DL (3840 x 2400)**
   - "DL" = Deep Learning - uses AI-powered scaling with ~half the performance cost of legacy DSR
5. Click **OK**
6. Click **Apply** in the main window

#### Step 2: Configure OBS for 4K Output

1. Open OBS Studio
2. Go to **Settings** → **Video**
3. Configure the following:

| Setting | Value |
|---------|-------|
| Base (Canvas) Resolution | 3840x2400 |
| Output (Scaled) Resolution | 3840x2160 (16:9 for YouTube) |
| Downscale Filter | Lanczos |
| FPS | 60 |

*NOTE: If the resolution 3840x2160 doesn't appear, just add it manually.*

4. Click **Apply** → **OK**

#### Step 3: Recording Settings (Recommended)

1. Go to **Settings** → **Output**
2. Set Output Mode to **Advanced**
3. Under **Recording** tab:
   - Encoder: NVIDIA NVENC H.264 (or HEVC for smaller files)
   - Rate Control: CQP
   - CQ Level: 18-20 (lower = better quality, larger files)

4. Click **Apply** → **OK**
