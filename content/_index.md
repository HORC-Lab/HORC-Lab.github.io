---
title: 'HUMAN ORIENTED ROBOTICS AND CONTROL (HORC) LAB'
summary: ''
date: 2026-01-01
type: landing

sections:
  # 1. Main Header, Carousel & Mission Section
  - block: markdown
    content:
      title: ''
      text: |
        <div style="text-align: center; margin-top: -6rem; margin-bottom: 2rem;">
        <img src="/uploads/media/HORC_Light.png" alt="HORC Lab Logo" style="max-width: 340px; width: 100%; height: auto; display: inline-block;" />
        </div>

        <div style="display: flex; flex-direction: row; align-items: flex-start; justify-content: center; gap: 2.5rem; flex-wrap: wrap;">

        <div style="flex: 1 1 350px; max-width: 480px; width: 100%;">
        <div class="horc-carousel-container">
        <div class="horc-carousel-slides">
        <div class="horc-slide active"><img src="/uploads/slide1.jpg" alt="Slide 1"></div>
        <div class="horc-slide"><img src="/uploads/slide2.jpg" alt="Slide 2"></div>
        <div class="horc-slide"><img src="/uploads/slide3.jpg" alt="Slide 3"></div>
        <div class="horc-slide"><img src="/uploads/slide4.jpg" alt="Slide 4"></div>
        <div class="horc-slide"><img src="/uploads/slide5.jpg" alt="Slide 5"></div>
        <div class="horc-slide"><img src="/uploads/slide6.jpg" alt="Slide 6"></div>
        <div class="horc-slide"><img src="/uploads/slide7.jpg" alt="Slide 7"></div>
        </div>
        <button class="horc-prev" onclick="changeHorcSlide(-1)">&#10094;</button>
        <button class="horc-next" onclick="changeHorcSlide(1)">&#10095;</button>
        <div class="horc-dots">
        <span class="horc-dot active" onclick="setHorcSlide(0)"></span>
        <span class="horc-dot" onclick="setHorcSlide(1)"></span>
        <span class="horc-dot" onclick="setHorcSlide(2)"></span>
        <span class="horc-dot" onclick="setHorcSlide(3)"></span>
        <span class="horc-dot" onclick="setHorcSlide(4)"></span>
        <span class="horc-dot" onclick="setHorcSlide(5)"></span>
        <span class="horc-dot" onclick="setHorcSlide(6)"></span>
        </div>
        </div>
        </div>

        <div style="flex: 1 1 550px; min-width: 280px;">
        <h2 style="margin-top: 0; font-size: 1.8rem; font-weight: 700;">Human-Oriented Robotics and Control Lab</h2>
        <p>Our research at the <strong style="color: #F97316;">interface of humans and robots</strong> is answering complex questions about the fundamentals of merging machine and human capabilities.</p>
        <p>The mission of the HORC Lab is to improve the quality of life and work by developing and controlling robotic devices that <strong style="color: #F97316;">physically and cognitively interact and collaborate with humans</strong>.</p>
        <p>This interaction can be found in devices that assist and augment human capabilities, as well as provide motor rehabilitation therapy to impaired individuals.</p>
        </div>

        </div>

        <style>
        .horc-carousel-container {
          position: relative;
          width: 100%;
          max-width: 480px;
          margin: 0 auto;
          overflow: hidden;
          border-radius: 10px;
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }
        .horc-carousel-slides {
          position: relative;
          width: 100%;
          height: 360px;
        }
        .horc-slide {
          display: none;
          width: 100%;
          height: 100%;
        }
        .horc-slide.active {
          display: block;
        }
        .horc-slide img {
          width: 100%;
          height: 100%;
          object-fit: contain;
          border-radius: 10px;
        }
        .horc-prev, .horc-next {
          position: absolute;
          top: 50%;
          transform: translateY(-50%);
          background: rgba(0, 0, 0, 0.5);
          color: white;
          border: none;
          padding: 10px 16px;
          font-size: 20px;
          cursor: pointer;
          border-radius: 50%;
          transition: background 0.3s;
          z-index: 10;
        }
        .horc-prev:hover, .horc-next:hover {
          background: rgba(0, 0, 0, 0.85);
        }
        .horc-prev { left: 15px; }
        .horc-next { right: 15px; }
        .horc-dots {
          text-align: center;
          position: absolute;
          bottom: 15px;
          width: 100%;
          z-index: 10;
        }
        .horc-dot {
          cursor: pointer;
          height: 12px;
          width: 12px;
          margin: 0 4px;
          background-color: rgba(255, 255, 255, 0.5);
          border-radius: 50%;
          display: inline-block;
          transition: background-color 0.3s;
        }
        .horc-dot.active, .horc-dot:hover {
          background-color: #ffffff;
        }
        </style>

        <script>
        (function() {
          let currentIndex = 0;
          let timer = null;

          window.showHorcSlide = function(index) {
            const slides = document.querySelectorAll('.horc-slide');
            const dots = document.querySelectorAll('.horc-dot');
            if (!slides.length) return;
            
            if (index >= slides.length) currentIndex = 0;
            else if (index < 0) currentIndex = slides.length - 1;
            else currentIndex = index;

            slides.forEach((slide, i) => {
              slide.classList.toggle('active', i === currentIndex);
            });
            dots.forEach((dot, i) => {
              dot.classList.toggle('active', i === currentIndex);
            });
          };

          window.changeHorcSlide = function(direction) {
            resetHorcTimer();
            showHorcSlide(currentIndex + direction);
          };

          window.setHorcSlide = function(index) {
            resetHorcTimer();
            showHorcSlide(index);
          };

          function resetHorcTimer() {
            clearInterval(timer);
            timer = setInterval(() => changeHorcSlide(1), 4000);
          }

          resetHorcTimer();
        })();
        </script>
    design:
      columns: '1'
      spacing:
        padding: ['5rem', '0', '0px', '0']  # Keeps top padding for logo position, removes bottom padding
  
  
  # Research Projects Block
  - block: portfolio
    id: projects
    content:
      title: Active Research Projects
      sort_by: Weight
      sort_ascending: true
      filters:
        folders:
          - project
      default_button_index: 0
    design:
      columns: '2'
      view: cards
      spacing:
        padding: ['0px', '0', '40px', '0']  # Starts immediately below Section 1 without extra gap


  # 2. Contact Section Below Everything
  - block: markdown
    id: contact
    content:
      title: Contact Us
      text: |
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; width: 100%; align-items: stretch;">

        <!-- Left Card: Locations -->
        <div style="background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 12px; padding: 1.5rem 1.25rem;">
        <h3 style="margin: 0 0 0.85rem 0; font-size: 1.45rem; font-weight: 700; color: #0284C7; line-height: 1.2;">Lab Locations</h3>
        <p style="margin: 0 0 0.65rem 0; font-size: 1.12rem; line-height: 1.35; white-space: nowrap;"><strong>Main Lab:</strong> 206 Spencer Lab, Newark, DE 19716</p>
        <p style="margin: 0; font-size: 1.12rem; line-height: 1.35; white-space: nowrap;"><strong>STAR Campus:</strong> 116 STAR Health Sciences Complex, Newark, DE 19716</p>
        </div>

        <!-- Right Card: Leadership & Contact -->
        <div style="background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.12); border-radius: 12px; padding: 1.5rem 1.25rem;">
        <h3 style="margin: 0 0 0.85rem 0; font-size: 1.45rem; font-weight: 700; color: #0284C7; line-height: 1.2;">Lab Leadership</h3>
        <p style="margin: 0 0 0.65rem 0; font-size: 1.12rem; line-height: 1.35; white-space: nowrap;"><strong>Director:</strong> Dr. Panos Artemiadis (Office: 331 Spencer Lab)</p>
        <p style="margin: 0; font-size: 1.12rem; line-height: 1.35; white-space: nowrap;"><strong>Email:</strong> <a href="mailto:partem@udel.edu" style="color: #0284C7; text-decoration: underline;">partem@udel.edu</a> &nbsp;|&nbsp; <strong>Phone:</strong> (302) 831-8546</p>
        </div>

        </div>
    design:
      columns: '1'
---