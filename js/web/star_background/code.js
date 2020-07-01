// Attribution: https://github.com/matteobruni/tsparticles

tsParticles.load("tsparticles", {
    fpsLimit: 60,
    interactivity: {
        detect_on: "canvas",
        events: {
            onclick: { enable: true, mode: "repulse" },
            onhover: {
                enable: true,
                mode: "bubble",
                parallax: { enable: false, force: 2, smooth: 10 }
            },
            resize: true
        },
        modes: {
            bubble: { distance: 200, duration: 2, opacity: 0, size: 0, speed: 3 },
            grab: { distance: 400, line_linked: { opacity: 1 } },
            push: { particles_nb: 4 },
            remove: { particles_nb: 2 },
            repulse: { distance: 400, duration: 0.4 }
        }
    },
    particles: {
        color: { value: "#ffffff" },
        line_linked: {
            color: "#ffffff",
            distance: 150,
            enable: false,
            opacity: 0.4,
            width: 1
        },
        move: {
            attract: { enable: false, rotateX: 600, rotateY: 600 },
            bounce: false,
            direction: "none",
            enable: true,
            out_mode: "out",
            random: true,
            speed: 0.3,
            straight: false
        },
        number: { density: { enable: true, value_area: 800 }, value: 600 },
        opacity: {
            anim: { enable: true, opacity_min: 0.3, speed: 5, sync: false },
            random: {
                enable: true,
                minimumValue: 0.3
            },
            value: 0.6
        },
        shape: {
            type: "circle"
        },
        size: {
            anim: { enable: false, size_min: 0.3, speed: 4, sync: false },
            random: false,
            value: 1
        }
    },
    retina_detect: true
});
