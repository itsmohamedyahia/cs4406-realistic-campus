# Realistic Virtual Campus Exploration (Production-Grade Three.js)

🌐 **Live Deployed Simulation:** [https://itsmohamedyahia.github.io/cs4406-realistic-campus/](https://itsmohamedyahia.github.io/cs4406-realistic-campus/)  
📦 **GitHub Repository:** [https://github.com/itsmohamedyahia/cs4406-realistic-campus](https://github.com/itsmohamedyahia/cs4406-realistic-campus)  
**Entry File:** [`index.html`](file:///s:/01_ACADEMIC_STUDY/UoPeople%20as%20Student/01_ACTIVE_COURSES/CS4406-Computer_Graphics/04_Unit%203_%20Viewing%20and%20Projection/coursework/realistic_campus/index.html)  

---

## 🌟 Overview & Architecture

Modeled after modern Three.js official examples (such as `webgl_animation_keyframes`), this standalone application elevates the virtual campus exploration experience into a production-grade WebGL simulation. It packages PBR materials, soft directional shadow cascades, physical sky radiance, and multi-tier procedural canvas textures into a single self-contained HTML file with **zero external image assets**, eliminating CORS restrictions while guaranteeing instant 60 FPS loading.

---

## 🚀 Key Graphics Engineering Features

1. **Modern ES Module Architecture (`<script type="importmap">`)**:
   - Uses Three.js r160, `OrbitControls`, and `RoomEnvironment` via standard CDN import maps.
   - 100% compliant with modern browsers and CodePen's native ES module runner.

2. **Physically Based Rendering (PBR) & Tone Mapping**:
   - **ACES Filmic Tone Mapping**: `renderer.toneMapping = THREE.ACESFilmicToneMapping` with `exposure: 1.05` for cinematic dynamic range.
   - **Soft Shadow Cascades**: `THREE.PCFSoftShadowMap` with a high-resolution $2048 \times 2048$ shadow camera, casting realistic soft shadows from building colonnades, trees, and streetlamps onto stone walkways.
   - **Physical Materials**: `MeshStandardMaterial` and `MeshPhysicalMaterial` featuring realistic roughness, metalness, and optical transmission (`ior: 1.52` for architectural glass; `ior: 1.33` for rippling fountain water).

3. **Procedural PBR Texture Generation (Self-Contained Canvas Contexts)**:
   - **Lawn Grass**: Multi-frequency organic noise with grass blade color jitter.
   - **Stone Pavers / Flagstones**: Beveled stone pavers with mortar grout lines and micro-grain speckling.
   - **Architectural Brick**: Crisp Flemish-bond brick coursing with bevels for neoclassical facades.
   - **Limestone / Marble**: Polished stone grain for Corinthian columns, entablatures, and fountain tiers.

4. **Rich Campus Architecture**:
   - **Central Neoclassical Administration Palace**: Terraced granite plinth, 4-tier grand entrance stairs, 6 fluted Corinthian columns with plinths and capitals, triangular pediment, dark slate mansard roof, and central clock cupola.
   - **Contemporary Science Complex**: Cantilevered structural wings, tinted glass curtain walls, horizontal metallic solar louvers (brise-soleil), and rooftop HVAC machinery.
   - **Grand Memorial Library**: Ashlar masonry, arched clerestory windows, and a standing-seam oxidized copper roof.
   - **Plaza & Promenade Amenities**: Tiered marble fountain with animated rippling water, cast-iron streetlamps with active warm point lights, granite curbstones, and organic deciduous trees with randomized multi-tier canopies.

---

## 🕹️ Interactive Pipeline Demonstration Modes

The floating glassmorphic navbar at the top allows instant switching between all 7 core graphics concepts:

| Button | Mode | Graphics Concept Demonstrated |
| :--- | :--- | :--- |
| **`🌐 Overview`** | Elevated Overview | High-angle isometric view displaying campus coordinates, camera eye position, and target look-at vector. |
| **`🚶 Campus Stroll`** | First-Person Walk | Pedestrian avenue stroll verifying that the dynamic View Matrix continuous mirrors user locomotion and gaze. |
| **`📐 Perspective`** | Perspective Projection | Natural 3-point perspective showing realistic foreshortening (distant Administration Palace shrinks with distance). |
| **`📏 Orthographic`** | Orthographic Projection | Parallel projection without depth foreshortening, demonstrating the flattening defect where buildings maintain uniform pixel scale. |
| **`✂️ Frustum Clipping`** | 6-Plane Viewing Frustum | Renders the active 3D camera frustum wireframe with near ($0.5\,\text{m}$) and far ($180\,\text{m}$) planes culling exterior geometry. |
| **`❌ Overlap Defect`** | Z-Buffer Disabled | Disables depth testing (`depthTest = false`), demonstrating the Painter's Algorithm flaw where a distant purple pavilion draws over a foreground tree. |
| **`✅ Z-Buffer Resolved`**| Hardware Z-Buffer Active | Activates hardware 24-bit depth testing (`depthTest = true`), demonstrating how per-fragment depth tests immediately restore correct surface occlusion. |

---

## 💻 How to Run & Test

### Option 1: Direct File Launch (Easiest)
Simply double-click or drag [`index.html`](file:///s:/01_ACADEMIC_STUDY/UoPeople%20as%20Student/01_ACTIVE_COURSES/CS4406-Computer_Graphics/04_Unit%203_%20Viewing%20and%20Projection/coursework/realistic_campus/index.html) into Google Chrome, Microsoft Edge, or Mozilla Firefox.

### Option 2: Run via PowerShell
```powershell
Start-Process "s:\01_ACADEMIC_STUDY\UoPeople as Student\01_ACTIVE_COURSES\CS4406-Computer_Graphics\04_Unit 3_ Viewing and Projection\coursework\realistic_campus\index.html"
```

### Option 3: Local Development Server
```powershell
python -m http.server 8080 --directory "s:\01_ACADEMIC_STUDY\UoPeople as Student\01_ACTIVE_COURSES\CS4406-Computer_Graphics\04_Unit 3_ Viewing and Projection\coursework\realistic_campus"
```
Then navigate to: `http://localhost:8080`

### Option 4: CodePen Deployment
1. Open a new pen at [CodePen.io](https://codepen.io/pen/).
2. Paste the contents of [`index.html`](file:///s:/01_ACADEMIC_STUDY/UoPeople%20as%20Student/01_ACTIVE_COURSES/CS4406-Computer_Graphics/04_Unit%203_%20Viewing%20and%20Projection/coursework/realistic_campus/index.html) directly into the HTML panel (or split into HTML/CSS/JS panels).
