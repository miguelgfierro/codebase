# Laptop display resolution

## Standard

1. Right-click your Desktop > Display Settings. 
2. In Display Resolution, change it to a 16:9 option like 2560x1440 (1440p) or 3840x2160 (4K). 
3. If 4K doesn't show up, click Advanced display settings > Display adapter properties > List All Modes to see every resolution your GPU can handle.

## GPU Scaling

If your laptop doesn't natively show "3840x2160" in the settings, use your GPU to force it.

On an MSI laptop, enable "Discrete Graphics Mode" (MUX Switch):

1. Launch MSI Center: Ensure you have the latest version installed.
2. Navigate to Features: Go to Features > User Scenario.
3. Select Graphics Mode: Look for the GPU Switch or Graphics Mode section.
4. Choose Discrete Graphics Mode: Select this mode and click OK.
5. Restart: Your laptop must restart for this change to take effect

Now force 4K Resolution:

1. Open NVIDIA Control Panel > Manage 3D Settings. 
2. Find `DSR - Factors` and check 2.25x DL (for AI-enhanced 4K). 
3. Apply this, then go back to Windows Display Settings—4K will now appear as an option.

*NOTE: In the laptop MSI Stealth A16 AI+, 4K is 3800x2400 (16:10), instead of the standard 3840x2160 (16:9).*

