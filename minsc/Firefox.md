# Firefox 

## Enable GPU 

Firefox doesn't use the GPU of your machine by default.

To benefit from using the GPU of your computer when using Firefox, go to the browser and type `about:config` then set the following flags:

```
gfx.webrenderer.all                 true
layers.acceleration.force-enabled   true
layers.omtp.enabled                 true
layout.display-list.retain          true
```

To check that Firefox is actually using the GPU, the first method is to check the GPU utilisation with methods like `nvidia-smi` or similar. Another way is to type in your browser `about:support`. In the section Graphics, you need to see:

* GPU: Active Yes
* HW_COMPOSITING: available by default, force_enabled by user:Force-enabled by pref 
* WEBRENDER: available by default, force_enabled by user:Force-enabled by pref, disabled by env: Not qualified
