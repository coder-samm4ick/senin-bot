< !DOCTYPE
html >
< html
lang = "uz" >

< head >
< meta
charset = "UTF-8" / >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0, viewport-fit=cover" / >
< script
src = "https://telegram.org/js/telegram-web-app.js" > < / script >
< script
type = "module"
src = "https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js" > < / script >
< title > Game
Service
WebApp < / title >
< style >
:root
{
    --bg:  # 061225;
        --bg - soft:  # 0b1b35;
--card:  # 101f3a;
--card - 2:  # 0d1a31;
--text:  # f7faff;
--text - soft:  # cfe0ff;
--text - muted:  # 91a4c8;
--line: rgba(148, 171, 215, .18);
--line - soft: rgba(255, 255, 255, .08);
--line - strong: rgba(255, 255, 255, .10);
--primary:  # 2f6bff;
--primary - hover:  # 5b8cff;
--primary - soft: rgba(47, 107, 255, .15);
--primary - border: rgba(47, 107, 255, .45);
--primary - border - strong: rgba(47, 107, 255, .75);
--primary - focus: rgba(47, 107, 255, .16);
--accent:  # 38bdf8;
--accent - soft: rgba(56, 189, 248, .10);
--danger:  # ef4444;
--danger - soft: rgba(239, 68, 68, .18);
--danger - border: rgba(239, 68, 68, .35);
--danger - border - strong: rgba(239, 68, 68, .9);
--danger - light:  # fecaca;
--success:  # 22c55e;
--success - soft: rgba(45, 226, 196, .10);
--success - light:  # bff6e9;
--warning:  # f59e0b;
--overlay: rgba(6, 18, 37, .82);
--overlay - soft: rgba(2, 8, 19, .60);
--overlay - dark: rgba(0, 0, 0, .34);
--surface - highlight: rgba(255, 255, 255, .22);
--surface - highlight - strong: rgba(255, 255, 255, .25);
--shadow: 0
16
px
44
px
rgba(0, 0, 0, .34);
--shadow - soft: 0
10
px
28
px
rgba(0, 0, 0, .22);
--shadow - primary: 0
10
px
24
px
rgba(47, 107, 255, .24);
--page - padding: 16
px;
--header - h: 72
px;
--nav - h: 78
px;
--blur: blur(18
px);
--ease: cubic - bezier(.2, .8, .2, 1);
}

*{
    box - sizing: border - box
}

html,
body
{
    margin: 0;
padding: 0;
min - height: 100 %;
background: var(--bg);
color: var(--text);
font - family: Inter, ui - sans - serif, system - ui, -apple - system, BlinkMacSystemFont, "Segoe UI", sans - serif;
overflow: hidden;
-webkit - tap - highlight - color: transparent;
-webkit - touch - callout: none;
-webkit - user - select: none;
user - select: none;
}

body
{
    display: flex;
justify - content: center;
align - items: stretch
}

button,
input
{
    font: inherit
}

button
{
    border: 0;
cursor: pointer;
transition: transform
.18
s
ease, box - shadow
.18
s
ease, opacity
.18
s
ease, background
.18
s
ease;
}

button: active
{
    transform: scale(.97)
}

.app - shell
{
    width: 100 %;
max - width: 720
px;
min - height: 100
vh;
position: relative;
overflow: hidden;
background: linear - gradient(180
deg, var(--bg - soft), var(--bg));
}

html,
body
{
    max - width: 100 %;
overflow - x: hidden
}

.app - shell
{
    overflow - x: hidden
}

.ambient,
.ambient::before,
.ambient::after
{
    content: "";
position: absolute;
border - radius: 999
px;
filter: blur(70
px);
pointer - events: none
}

.ambient
{
    inset: 0;
z - index: 0
}

.ambient::before
{
    width: 220px;
height: 220
px;
background: var(--primary - soft);
top: -40
px;
right: -70
px
}

.ambient::after
{
    width: 180px;
height: 180
px;
background: var(--accent - soft);
bottom: 90
px;
left: -80
px
}

.topbar
{
    height: var(--header - h);
position: sticky;
top: 0;
z - index: 20;
display: flex;
align - items: center;
justify - content: space - between;
padding: 14
px
16
px;
background: var(--overlay);
backdrop - filter: var(--blur);
border - bottom: 1
px
solid
var(--line);
}

.brand
{
    display: flex;
align - items: center;
gap: 12
px;
min - width: 0
}

.avatar
{
    width: 38px;
height: 38
px;
border - radius: 50 %;
display: grid;
place - items: center;
font - weight: 800;
background: linear - gradient(135
deg, var(--card), var(--card - 2));
border: 1
px
solid
var(--line);
overflow: hidden;
}

.brand - title
{
    font - size: 16px;
font - weight: 700;
white - space: nowrap;
overflow: hidden;
text - overflow: ellipsis
}

.brand - subtitle
{
    font - size: 12px;
color: var(--text - muted);
margin - top: 2
px
}

.balance - chip
{
    display: inline - flex;
align - items: center;
gap: 8
px;
padding: 10
px
14
px;
border - radius: 16
px;
background: linear - gradient(135
deg, var(--primary), var(--primary - hover));
box - shadow: var(--shadow - primary);
font - size: 14
px;
font - weight: 700;
color: var(--text)
}

.coin
{
    width: 18px;
height: 18
px;
border - radius: 50 %;
background: radial - gradient(circle
at
35 % 30 %,  # ffe89a, #ffca29 62%, #e59f00 100%);
position: relative;
flex: 0
0
auto
}

.coin::after
{
    content: "";
position: absolute;
inset: 5
px;
border - radius: 50 %;
background: var(--surface - highlight - strong)
}

.view - stack
{
    position: relative;
z - index: 1;
min - height: calc(100
vh - var(--header - h) - var(--nav - h))
}

.page
{
    position: absolute;
inset: 0;
padding: 16
px
16
px
calc(var(--nav - h) + 22
px);
overflow - y: auto;
opacity: 0;
pointer - events: none;
transform: translateX(28
px) scale(.985);
transition: opacity
.34
s
var(--ease), transform
.42
s
var(--ease), filter
.34
s
var(--ease);
filter: blur(10
px);
scrollbar - width: none
}

.none
{
    display: none
}

.page::-webkit - scrollbar
{
    display: none
}

.page.active
{
    opacity: 1;
pointer - events: auto;
transform: translateX(0)
scale(1);
filter: blur(0)
}

.page.exit - left
{
    transform: translateX(-22px) scale(.985);
opacity: 0;
filter: blur(8
px)
}

.game - card,
.product - card,
.cart - card,
.profile - card,
.summary - box,
.detail - card,
.info - box,
.status - card,
.status - modal,
.banner - slider
{
    background: linear - gradient(180deg, var(--card), var(--card - 2));
border: 1
px
solid
var(--line);
box - shadow: var(--shadow - soft)
}

.section
{
    margin - top: 20px
}

.section - title
{
    margin: 0;
font - size: 24
px;
line - height: 1.08;
letter - spacing: -.03
em
}

.section - head,
.game - meta,
.meta - row,
.summary - row,
.price - line,
.checkout - total,
.detail - heading,
.profile - card,
.cart - card
{
    display: flex;
align - items: center;
justify - content: space - between;
gap: 12
px
}

.section - head
{
    margin - bottom: 14px
}

# bannerSection .section-head {
margin - top: 0
}

.muted,
.helper - text,
.tiny - note,
.brand - subtitle,
.cart - sub,
.profile - desc,
.qty - tag,
.payment - card
span,
.package - btn
span,
.info - box
span,
.banner - content
span
{
    color: var(--text - muted);
line - height: 1.5;
font - size: 12
px
}

.link - btn
{
    background: transparent;
color: var(--primary - hover);
font - size: 13
px;
font - weight: 700;
padding: 4
px
0
}

.banner - slider
{
    position: relative;
border - radius: 24
px;
overflow: hidden;
height: 180
px
}

.banner - track
{
    position: relative;
width: 100 %;
height: 100 %;
perspective: 900
px;
will - change: transform
}

.banner - slide
{
    position: absolute;
inset: 0;
opacity: 0;
padding: 18
px;
display: flex;
align - items: flex - end;
overflow: hidden;
backface - visibility: hidden;
transform: translateZ(0)
}

.banner - slide::before
{
    content: "";
position: absolute;
inset: 0;
background - image: linear - gradient(rgba(8, 16, 34, .20), rgba(8, 16, 34, .38)), var(--banner - image);
background - size: cover;
background - position: center;
transform: scale(1);
will - change: transform, opacity
}

.banner - slider.banner - style - 1.banner - slide
{
    z - index: 0;
opacity: 0;
pointer - events: none;
transition: opacity
.56
s
ease
}

.banner - slider.banner - style - 1.banner - slide.active
{
    z - index: 2;
opacity: 1;
pointer - events: auto
}

.banner - slider.banner - style - 1.banner - slide. is -leaving
{
    z - index: 1;
opacity: 0
}

.banner - slider.banner - style - 1.banner - slide. is -entering::before
{
    animation: banner - enter - zoom .68s var(--ease) both
}


@keyframes


banner - enter - zoom
{
from

{transform: scale(1.055);
opacity: .72}
to
{transform: scale(1);
opacity: 1}
}

# bannerSection.banner-layout-expanded {
padding - inline: 8
px
}

# bannerSection.banner-layout-style-2 {
width: 100 %;
max - width: 100 %;
overflow - x: hidden;
contain: paint;
padding - inline: 0
}

.banner - slider.banner - style - 3
{
    overflow: visible;
background: none;
border: none;
box - shadow: none
}

.banner - slider.banner - style - 2
{
    overflow: hidden;
width: 100 %;
max - width: 100 %;
background: none;
border: none;
box - shadow: none;
contain: paint
}

.banner - slider.banner - style - 2.banner - track
{
    display: flex;
width: 100 %;
max - width: 100 %;
gap: 12
px;
will - change: transform;
transform: translate3d(0, 0, 0)
}

.banner - slider.banner - style - 2.banner - slide
{
    position: relative;
inset: auto;
flex: 0
0
100 %;
min - width: 100 %;
width: 100 %;
max - width: 100 %;
min - width: 0;
height: 100 %;
opacity: 1;
pointer - events: auto;
border - radius: 20
px;
box - shadow: var(--shadow - soft)
}

.banner - slider.banner - style - 2.banner - content
strong
{
    opacity: 0;
transform: translateY(14
px)
}

.banner - slider.banner - style - 2.banner - content
span
{
    opacity: 0;
transform: translateY(10
px)
}

.banner - slider.banner - style - 2.banner - slide.active.banner - content
strong,
.banner - slider.banner - style - 2.banner - slide.active.banner - content
span
{
    opacity: 1;
transform: translateY(0)
}

.banner - slider.banner - style - 2. is -sliding.banner - slide.banner - content
strong,
.banner - slider.banner - style - 2. is -sliding.banner - slide.banner - content
span
{
    opacity: 0;
transform: translateY(10
px)
}

.banner - slider.banner - style - 2.banner - content.text - enter
strong
{
    animation: banner - title - enter .44s cubic - bezier(.2, .8, .2, 1) both
}

.banner - slider.banner - style - 2.banner - content.text - enter
span
{
    animation: banner - subtitle - enter .44s 120ms cubic - bezier(.2, .8, .2, 1) both
}

@ keyframes
banner - title - enter
{
from

{opacity: 0;
transform: translateY(14
px)}
to
{opacity: 1;
transform: translateY(0)}
}

@keyframes


banner - subtitle - enter
{
from

{opacity: 0;
transform: translateY(10
px)}
to
{opacity: 1;
transform: translateY(0)}
}

.banner - slider.banner - style - 3.banner - slide
{
    inset: 10px 34px;
border - radius: 20
px;
border: 1
px
solid
transparent;
opacity: 0;
pointer - events: none;
filter: blur(2
px);
transform: translateX(0)
scale(.78)
translateZ(-70
px);
transition: opacity
.62
s
var(--ease), transform
.68
s
var(--ease), filter
.62
s
ease, box - shadow
.62
s
ease, border - color
.62
s
ease
}

.banner - slider.banner - style - 3.banner - slide.prev
{
    z - index: 1;
opacity: .46;
filter: blur(1.5
px);
transform: translateX(-18 %)
scale(.86)
translateZ(-38
px)
}

.banner - slider.banner - style - 3.banner - slide.next
{
    z - index: 1;
opacity: .46;
filter: blur(1.5
px);
transform: translateX(18 %)
scale(.86)
translateZ(-38
px)
}

.banner - slider.banner - style - 3.banner - slide.active
{
    z - index: 3;
opacity: 1;
pointer - events: auto;
filter: none;
border - color: var(--primary - border);
box - shadow: 0
12
px
32
px
rgba(47, 107, 255, .28), 0
0
20
px
rgba(56, 189, 248, .12);
transform: translateX(0)
scale(1)
translateZ(0)
}

.banner - slider.banner - style - 3. is -single.banner - slide.active
{
    inset: 0;
border - color: transparent;
box - shadow: none
}

.banner - slide.has - link
{
    cursor: pointer
}

.banner - slide::after
{
    content: "";
position: absolute;
inset: 0;
background: linear - gradient(180
deg, rgba(5, 12, 26, .08), rgba(5, 12, 26, .48))
}

.banner - content
{
    position: relative;
z - index: 1;
display: flex;
flex - direction: column;
gap: 6
px;
max - width: 78 %
}

.banner - content
strong
{
    font - size: 22px;
line - height: 1.08;
letter - spacing: -.03
em
}

.banner - content
span
{
    color: var(--text);
font - size: 13
px
}

.slider - nav
{
    position: absolute;
top: 50 %;
transform: translateY(-50 %) !important;
width: 40
px;
height: 40
px;
border - radius: 14
px;
background: rgba(7, 15, 32, .52);
border: 1
px
solid
var(--line - soft);
color: var(--text);
font - size: 26
px;
z - index: 8;
display: grid;
place - items: center;
backdrop - filter: blur(8
px)
}

.slider - nav.prev
{
    left: 10px
}

.slider - nav.next
{
    right: 10px
}

.banner - dots
{
    display: flex;
justify - content: center;
gap: 8
px;
margin - top: 10
px
}

.banner - dot
{
    width: 8px;
height: 8
px;
border - radius: 999
px;
background: var(--surface - highlight)
}

.banner - dot.active
{
    width: 22px;
background: linear - gradient(135
deg, var(--primary), var(--primary - hover))
}

.categories
{
    display: flex;
gap: 10
px;
scrollbar - width: none;
padding - bottom: 2
px
}

.categories::-webkit - scrollbar
{
    display: none
}

.chip
{
    white - space: nowrap;
padding: 11
px
14
px;
border - radius: 999
px;
background: var(--line - soft);
color: var(--text - soft);
border: 1
px
solid
var(--line - soft);
font - size: 13
px;
font - weight: 700
}

.chip.active
{
    background: linear - gradient(135deg, var(--primary), var(--primary - hover));
color: var(--text);
box - shadow: var(--shadow - primary)
}

.game - strip,
.products,
.package - list,
.payment - grid,
.detail - info - grid,
.topup - amounts
{
    display: grid;
grid - template - columns: repeat(2, minmax(0, 1
fr));
gap: 14
px
}

.detail - info - grid
{
    grid - template - columns: repeat(3, minmax(0, 1fr))
}

.game - card,
.product - card,
.cart - card,
.profile - card,
.summary - box,
.detail - card,
.profile - hero
{
    border - radius: 22px;
padding: 14
px
}

.summary - box,
.detail - card,
.profile - hero
{
    margin: 14px 0
}

.game - card
{
    overflow: hidden
}

.game - card. is -selected
{
    border - color: var(--primary - border);
box - shadow: var(--shadow - soft)
}

.game - cover,
.product - thumb
{
    border - radius: 18px;
position: relative;
overflow: hidden
}

.game - cover
{
    height: 150px;
display: flex;
align - items: flex - end;
padding: 12
px;
background: linear - gradient(160
deg, rgba(80, 110, 255, .36), rgba(19, 29, 52, .2));
margin - bottom: 12
px
}

.game - cover::before
{
    content: "";
position: absolute;
inset: 0;
background:
radial - gradient(circle
at
25 % 20 %, rgba(255, 255, 255, .20), transparent
28 %),
radial - gradient(circle
at
78 % 30 %, rgba(45, 226, 196, .14), transparent
22 %),
linear - gradient(180
deg, transparent
0 %, var(--overlay - dark)
100 %)
}

.game - logo,
.detail - banner.badge
{
    position: relative;
z - index: 1;
background: var(--line - strong);
backdrop - filter: blur(10
px);
border: 1
px
solid
var(--line - strong);
overflow: hidden;
display: grid;
place - items: center
}

.game - logo
{
    width: 56px;
height: 56
px;
border - radius: 18
px;
padding: 8
px
}

.detail - banner.badge
{
    width: 64px;
height: 64
px;
border - radius: 20
px;
padding: 8
px
}

.game - logo
img,
.product - thumb
img,
.cart - thumb
img,
.detail - banner.badge
img
{
    width: 100 %;
height: 100 %;
object - fit: cover;
display: block;
border - radius: inherit
}

.floating - badge,
.pill
{
    display: inline - flex;
align - items: center;
gap: 6
px;
padding: 7
px
10
px;
border - radius: 999
px;
font - size: 12
px;
font - weight: 700;
white - space: nowrap
}

.floating - badge
{
    position: absolute;
top: 14
px;
right: 14
px;
background: rgba(9, 18, 37, .72);
border: 1
px
solid
var(--line - soft);
color: var(--text - soft);
backdrop - filter: blur(8
px)
}

.pill
{
    background: var(--line - soft);
color: var(--text - soft)
}

.pill.success
{
    color: var(--success - light);
background: var(--success - soft)
}

.game - title,
.product - title,
.cart - title,
.profile - name - row
{
    font - size: 16px;
font - weight: 800;
line - height: 1.25
}

.product - thumb
{
    height: 120px;
display: grid;
place - items: center;
margin - bottom: 12
px;
background: linear - gradient(160
deg, var(--primary - soft), rgba(24, 34, 58, .2));
padding: 10
px
}

.product - thumb::after
{
    content: "";
position: absolute;
width: 90
px;
height: 90
px;
border - radius: 50 %;
background: var(--line - soft);
top: -18
px;
right: -14
px
}

.price
{
    margin - top: 8px;
font - size: 20
px;
font - weight: 900;
letter - spacing: -.03
em
}

.price
small
{
    font - size: 12px;
color: var(--text - muted);
font - weight: 700;
margin - left: 4
px
}

.icon - btn
{
    width: 42px;
height: 42
px;
border - radius: 14
px;
background: var(--line - soft);
color: var(--text);
display: grid;
place - items: center;
font - size: 18
px;
border: 1
px
solid
var(--line - soft)
}

.cart - list,
.profile - list
{
    display: flex;
flex - direction: column;
gap: 14
px
}

.cart - thumb
{
    width: 74px;
height: 74
px;
border - radius: 20
px;
display: grid;
place - items: center;
background: linear - gradient(160
deg, var(--primary - soft), rgba(22, 35, 63, .3));
flex: 0
0
auto;
overflow: hidden;
padding: 10
px
}

.cart - content
{
    flex: 1;
min - width: 0
}

.stepper
{
    display: inline - flex;
align - items: center;
gap: 8
px;
background: var(--line - soft);
border - radius: 14
px;
padding: 6
px;
margin - top: 10
px
}

.stepper
button
{
    width: 28px;
height: 28
px;
border - radius: 10
px;
background: var(--line - soft);
color: var(--text);
font - weight: 900
}

.stepper
span
{
    min - width: 22px;
text - align: center;
font - weight: 700;
font - size: 14
px
}

.summary - row,
.status - row
{
    padding: 10px 0;
border - bottom: 1
px
solid
var(--line - soft);
color: var(--text - soft);
font - size: 14
px
}

.status - row
{
    display: flex;
align - items: center;
justify - content: space - between;
gap: 12
px
}

.status - row
span
{
    min - width: 0
}

.status - row
strong
{
    min - width: 0;
text - align: right;
overflow - wrap: anywhere
}

.summary - row: last - child,
.status - row: last - child
{
    border - bottom: 0
}

.profile - hero
{
    text - align: center;
padding: 18
px
}

.profile - avatar
{
    width: 92px;
height: 92
px;
border - radius: 50 %;
margin: 4
px
auto
14
px;
display: grid;
place - items: center;
font - size: 34
px;
font - weight: 800;
background: linear - gradient(135
deg,  # 213760, #0e1d39 60%, #18294c);
border: 1
px
solid
var(--line - strong);
overflow: hidden;
}

.profile - avatar
img,
.avatar
img
{
width: 100 %;
}

.profile - name
{
font - size: 24
px;
font - weight: 900;
letter - spacing: -.03
em
}

.profile - id
{
margin - top: 6
px;
color: var(--text - muted);
font - size: 13
px
}

.profile - left
{
display: flex;
align - items: center;
gap: 12
px
}

.profile - card.actionable
{
cursor: pointer
}

.profile - card.referral - card
{
background: linear - gradient(135
deg, rgba(47, 107, 255, .22), rgba(56, 189, 248, .08), var(--card - 2));
border - color: var(--primary - border);
box - shadow: var(--shadow - soft), 0
0
20
px
rgba(47, 107, 255, .12)
}

.referral - modal
{
max - height: 84
vh;
overflow: hidden;
display: flex;
flex - direction: column;
gap: 12
px
}

.referral - stats
{
display: grid;
grid - template - columns: repeat(2, minmax(0, 1
fr));
gap: 10
px
}

.referral - stat,
.referral - link - box
{
padding: 12
px;
border - radius: 16
px;
background: var(--line - soft);
border: 1
px
solid
var(--line)
}

.referral - stat
strong
{
display: block;
margin - top: 5
px;
font - size: 17
px
}

.referral - link
{
margin - top: 6
px;
color: var(--text - soft);
font - size: 12
px;
overflow: hidden;
white - space: nowrap;
text - overflow: ellipsis
}

.referral - actions
{
display: grid;
grid - template - columns: 1
fr
1
fr;
gap: 10
px
}

.referral - list
{
overflow - y: auto;
display: grid;
gap: 8
px;
scrollbar - width: none
}

.referral - list::-webkit - scrollbar
{
display: none
}

.referral - person
{
display: flex;
justify - content: space - between;
align - items: center;
gap: 12
px;
padding: 11
px
12
px;
border - radius: 14
px;
background: var(--line - soft);
border: 1
px
solid
var(--line)
}

.referral - person
span
{
display: flex;
flex - direction: column;
gap: 3
px;
min - width: 0
}

.referral - person
b
{
font - size: 13
px;
font - weight: 800;
overflow: hidden;
text - overflow: ellipsis;
white - space: nowrap
}

.referral - person
small
{
color: var(--text - muted);
font - size: 11
px
}

.referral - person
strong
{
color: var(--success - light);
white - space: nowrap
}

.profile - circle
{
width: 42
px;
height: 42
px;
border - radius: 14
px;
display: grid;
place - items: center;
background: var(--primary - soft);
color: var(--text - soft);
font - size: 18
px;
border: 1
px
solid
var(--line)
}

.history - tabs
{
display: flex;
gap: 10
px;
margin - bottom: 12
px;
}

.history - tab
{
flex: 1;
padding: 10
px;
border - radius: 14
px;
background: var(--line - soft);
border: 1
px
solid
var(--line);
color: var(--text);
font - weight: 700;
}

.history - tab.active
{
background: linear - gradient(135
deg, var(--primary), var(--primary - hover));
}

.history - filters
{
display: flex;
gap: 8
px;
overflow - x: auto;
margin - bottom: 12
px;
}

.filter - chip
{
padding: 6
px
12
px;
border - radius: 999
px;
background: var(--line - soft);
border: 1
px
solid
var(--line);
font - size: 12
px;
color: var(--text);
}

.filter - chip.active
{
background: var(--primary - soft);
border - color: var(--primary - border);
}

.history - item
{
padding: 12
px;
border - radius: 14
px;
background: var(--line - soft);
border: 1
px
solid
var(--line);
margin - bottom: 10
px;
}

.history - status
{
font - size: 12
px;
margin - top: 4
px;
line - height: 1.35;
overflow - wrap: anywhere;
}

.status - success
{
color: var(--success);
}

.status - pending
{
color: var(--warning);
}

.status - processing
{
color: var(--warning);
}

.status - failed
{
color: var(--danger);
}

.status - cancel
{
color: var(--danger);
}

.status - expired
{
color: var(--warning);
}

.history - row
{
display: flex;
justify - content: space - between;
align - items: center;
gap: 12
px;
}

.history - left
{
display: flex;
align - items: center;
gap: 12
px;
}

.history - img
{
width: 46
px;
height: 46
px;
border - radius: 12
px;
object - fit: cover;
}

.history - title
{
font - weight: 700;
font - size: 15
px;
}

.history - right
{
text - align: right;
display: flex;
flex - direction: column;
gap: 4
px;
max - width: 50 %;
}

.history - price
{
margin - top: 5
px;
font - weight: 800;
font - size: 13
px;
}

.history - status
{
font - size: 12
px;
}

.history - time
{
font - size: 13
px;
font - weight: 700;
opacity: 0.8;
}

.value
{
color: var(--text - soft);
font - size: 14
px;
font - weight: 700;
white - space: nowrap
}

.topup - chip
{
min - height: 44
px;
border - radius: 14
px;
background: var(--line - soft);
color: var(--text);
border: 1
px
solid
var(--line);
font - size: 16
px;
font - weight: 800;
letter - spacing: 0
}

.topup - chip.active,
.package - btn.active,
.payment - card.active
{
background: var(--primary - soft);
border - color: var(--primary - border);
box - shadow: var(--shadow - soft)
}

.balance - methods.payment - card
strong
{
font - size: 18
px
}

.bottom - nav
{
position: fixed;
left: 50 %;
transform: translateX(-50 %);
bottom: 0;
width: 100 %;
max - width: 720
px;
height: var(--nav - h);
padding: 10
px
14
px
calc(10
px + env(safe - area - inset - bottom, 0
px));
background: rgba(7, 17, 36, .82);
backdrop - filter: var(--blur);
border - top: 1
px
solid
var(--line);
z - index: 25
}

.nav - grid
{
height: 100 %;
display: grid;
grid - template - columns: repeat(4, 1
fr);
gap: 8
px
}

.nav - item
{
position: relative;
display: flex;
flex - direction: column;
align - items: center;
justify - content: center;
gap: 5
px;
color: var(--text - muted);
border - radius: 18
px;
background: transparent;
font - size: 12
px;
font - weight: 700
}

.nav - item.icon
{
font - size: 18
px;
line - height: 1
}

.nav - item.active
{
color: var(--text)
}

.nav - item.active::before
{
content: "";
position: absolute;
inset: 2
px;
border - radius: 16
px;
background: var(--primary - soft);
border: 1
px
solid
var(--primary - border);
z - index: -1;
box - shadow: var(--shadow - soft)
}

.detail - panel - backdrop,
.checkout - panel - backdrop,
.overlay - backdrop
{
position: fixed;
inset: 0;
background: var(--overlay - soft);
backdrop - filter: blur(6
px);
opacity: 0;
pointer - events: none;
transition: opacity
.28
s
ease
}

.detail - panel - backdrop,
.checkout - panel - backdrop
{
z - index: 40
}

.overlay - backdrop
{
z - index: 70
}

.detail - panel - backdrop.show,
.checkout - panel - backdrop.show,
.overlay - backdrop.show
{
opacity: 1;
pointer - events: auto
}

.detail - panel,
.checkout - panel
{
position: fixed;
left: 50 %;
bottom: 0;
width: 100 %;
max - width: 720
px;
max - height: 88
vh;
transform: translateX(-50 %)
translateY(100 %);
transition: transform
.38
s
var(--ease);
background: linear - gradient(180
deg, rgba(12, 23, 44, .98), rgba(8, 18, 36, .99));
border - top - left - radius: 30
px;
border - top - right - radius: 30
px;
border: 1
px
solid
var(--line - soft);
box - shadow: var(--shadow);
z - index: 50;
overflow: hidden
}

.detail - panel.show,
.checkout - panel.show
{
transform: translateX(-50 %)
translateY(0)
}

.detail - panel.dragging,
.checkout - panel.dragging
{
transition: none !important;
}

.detail - panel.grabber,
.checkout - panel.grabber
{
touch - action: none;
cursor: grab;
}

.detail - panel.dragging.grabber,
.checkout - panel.dragging.grabber
{
cursor: grabbing;
}

.detail - panel - backdrop,
.checkout - panel - backdrop,
.overlay - backdrop
{
position: fixed;
inset: 0;
background: var(--overlay - soft);
backdrop - filter: blur(6
px);
opacity: 0;
pointer - events: none;
transition: opacity
.22
s
ease, backdrop - filter
.22
s
ease;
}

.detail - game - header
{
display: flex;
align - items: center;
gap: 14
px;
padding: 14
px
0
4
px;
}

.detail - game - icon - wrap
{
width: 64
px;
height: 64
px;
border - radius: 18
px;
overflow: hidden;
flex: 0
0
auto;
background: var(--line - soft);
border: 1
px
solid
var(--line - soft);
padding: 6
px;
}

.detail - game - icon
{
width: 100 %;
height: 100 %;
object - fit: cover;
border - radius: 14
px;
display: block;
}

.detail - game - info
{
flex: 1;
min - width: 0;
}

.detail - game - name
{
font - size: 18
px;
font - weight: 800;
line - height: 1.15;
}

.detail - game - desc
{
margin - top: 4
px;
font - size: 13
px;
color: var(--text - muted);
line - height: 1.4;
}

.package - top
{
display: flex;
align - items: center;
gap: 10
px;
margin - bottom: 8
px;
}

.package - img
{
width: 40
px;
height: 40
px;
border - radius: 12
px;
object - fit: cover;
flex: 0
0
auto;
background: var(--line - soft);
}

.package - text
{
min - width: 0;
flex: 1;
}

/ *scrollable
part * /
.payment - modal
{
position: fixed;
inset: 0;
background: var(--bg);
backdrop - filter: blur(10
px);
z - index: 25;
display: none;
color: var(--text);
}

.payment - modal.show
{
display: block;
}

.payment - container
{
max - width: 520
px;
margin: 0
auto;
min - height: 100
vh;
height: 100
dvh;
display: flex;
flex - direction: column;
position: relative;
overflow: hidden;
}

.payment - container::before
{
content: "";
position: absolute;
inset: 0
0
auto;
height: 180
px;
background: linear - gradient(180
deg, var(--primary - focus), transparent);
pointer - events: none;
}

.payment - scroll
{
flex: 1
1
auto;
min - height: 0;
overflow - y: auto;
padding: 14
px
16
px
18
px;
display: grid;
gap: 12
px;
position: relative;
z - index: 1;
scrollbar - width: none;
}

.payment - scroll::-webkit - scrollbar
{
display: none
}

.payment - header
{
display: flex;
align - items: center;
justify - content: space - between;
gap: 12
px;
padding - top: 4
px;
}

.payment - close - btn
{
width: 40
px;
height: 40
px;
display: grid;
place - items: center;
border - radius: 14
px;
background: var(--line - soft);
border: 1
px
solid
var(--line);
color: var(--text);
font - size: 18
px;
}

.payment - title
{
flex: 1;
min - width: 0;
}

.payment - title
h3
{
margin: 0;
font - size: 18
px;
line - height: 1.2;
}

.payment - title
span
{
display: block;
margin - top: 3
px;
font - size: 12
px;
color: var(--text - muted);
}

.payment - status - pill
{
padding: 8
px
10
px;
border - radius: 999
px;
background: var(--primary - soft);
border: 1
px
solid
var(--primary - border);
color: var(--text - soft);
font - size: 12
px;
font - weight: 800;
white - space: nowrap;
}

.payment - status - pill.expired
{
background: var(--danger - soft);
border - color: var(--danger - border - strong);
color: var(--danger - light);
}

.payment - hero
{
display: grid;
gap: 12
px;
}

.payment - amount - card,
.payment - timer - card,
.payment - info - card
{
border: 1
px
solid
var(--line);
background: linear - gradient(180
deg, var(--card), var(--card - 2));
box - shadow: var(--shadow - soft);
backdrop - filter: blur(10
px);
}

.payment - amount - card
{
border - radius: 24
px;
padding: 18
px;
position: relative;
overflow: hidden;
}

.payment - amount - card::after
{
display: none;
}

.payment - amount - label
{
font - size: 13
px;
color: var(--text - muted);
font - weight: 700;
}

.payment - amount - row
{
display: flex;
align - items: center;
justify - content: space - between;
gap: 12
px;
margin - top: 8
px;
position: relative;
z - index: 1;
}

.payment - amount - row
strong
{
font - size: 34
px;
letter - spacing: 0;
line - height: 1.05;
color: var(--text);
}

.payment - copy - btn,
.payment - card - copy
{
width: 42
px;
height: 42
px;
border - radius: 14
px;
display: grid;
place - items: center;
color: var(--text);
background: var(--primary - soft);
border: 1
px
solid
var(--primary - border);
}

.payment - amount - subtitle
{
margin - top: 8
px;
font - size: 13
px;
color: var(--text - muted);
}

.payment - timer - card
{
border - radius: 20
px;
padding: 14
px;
}

.payment - timer - top
{
display: flex;
justify - content: space - between;
align - items: center;
color: var(--text - muted);
font - size: 13
px;
font - weight: 700;
}

.payment - timer - top
strong
{
font - size: 22
px;
color: var(--accent);
letter - spacing: 0;
}

.payment - timer - card.expired.payment - timer - top
strong
{
color: var(--danger - light);
}

.payment - progress
{
margin - top: 12
px;
height: 8
px;
overflow: hidden;
border - radius: 999
px;
background: var(--line - soft);
}

.payment - progress - fill
{
width: 100 %;
height: 100 %;
border - radius: inherit;
background: linear - gradient(90
deg, var(--primary), var(--accent));
transition: width
.25
s
linear;
}

.payment - timer - card.expired.payment - progress - fill
{
background: var(--danger);
}

.payment - card - slider
{
display: grid;
gap: 9
px;
}

.payment - section - title
{
display: flex;
justify - content: space - between;
align - items: center;
font - size: 13
px;
color: var(--text - muted);
font - weight: 800;
}

.payment - card - count
{
color: var(--text - muted);
font - weight: 700;
}

.card - track
{
display: flex;
gap: 14
px;
overflow - x: auto;
scroll - snap - type: x
mandatory;
padding: 2
px
2
px
8
px;
scroll - padding - left: 2
px;
scrollbar - width: none;
}

.card - track::-webkit - scrollbar
{
display: none
}

.payment - bank - card
{
min - width: 86 %;
flex - shrink: 0;
scroll - snap - align: center;
position: relative;
overflow: hidden;
padding: 18
px;
min - height: 172
px;
border - radius: 24
px;
border: 1
px
solid
var(--line);
background: linear - gradient(135
deg, var(--card), var(--bg - soft));
color: var(--text);
box - shadow: var(--shadow - soft);
}

.payment - bank - card.active
{
border - color: var(--primary - border - strong);
box - shadow: var(--shadow - soft), inset
0
0
0
1
px
var(--primary - border);
}

.payment - bank - card::after
{
content: "";
position: absolute;
right: -30
px;
bottom: -36
px;
width: 130
px;
height: 130
px;
border - radius: 50 %;
background: var(--line - soft);
}

.payment - card - top
{
display: flex;
justify - content: space - between;
gap: 12
px;
color: var(--text);
font - size: 13
px;
font - weight: 800;
}

.card - badge
{
padding: 4
px
8
px;
border - radius: 999
px;
background: var(--line - soft);
color: var(--text);
font - size: 11
px;
}

.payment - card - number
{
margin: 24
px
46
px
18
px
0;
font - size: 22
px;
line - height: 1.25;
font - weight: 900;
letter - spacing: 1
px;
word - spacing: 4
px;
}

.payment - card - owner
{
color: var(--text - muted);
font - size: 13
px;
text - transform: uppercase;
letter - spacing: .04
em;
}

.payment - card - copy
{
position: absolute;
right: 16
px;
top: 68
px;
z - index: 1;
}

.card - dots
{
display: flex;
justify - content: center;
gap: 6
px;
margin - top: 2
px;
}

.dot
{
width: 6
px;
height: 6
px;
border - radius: 50 %;
background: rgba(145, 164, 200, .34);
transition: width
.18
s, background
.18
s;
}

.dot.active
{
width: 18
px;
border - radius: 10
px;
background: var(--primary);
}

.payment - info - card
{
border - radius: 20
px;
padding: 14
px;
display: flex;
flex - direction: column;
gap: 10
px;
}

.payment - step
{
display: flex;
align - items: center;
gap: 10
px;
color: var(--text);
font - size: 13
px;
}

.payment - step
span
{
width: 26
px;
height: 26
px;
display: grid;
place - items: center;
border - radius: 10
px;
background: var(--primary - soft);
color: var(--text - soft);
font - weight: 900;
flex: 0
0
auto;
}

.payment - footer
{
flex: 0
0
auto;
position: relative;
z - index: 2;
padding: 12
px
16
px
calc(12
px + env(safe - area - inset - bottom, 0
px));
background: linear - gradient(180
deg, var(--overlay - soft), var(--bg));
backdrop - filter: blur(16
px);
border - top: 1
px
solid
var(--line);
}

.payment - footer - actions
{
display: grid;
grid - template - columns: 1
fr
1
fr;
gap: 10
px;
}

.pay - btn,
.payment - cancel - btn
{
width: 100 %;
height: 52
px;
border - radius: 16
px;
font - weight: 800;
font - size: 16
px;
}

.pay - btn
{
background: linear - gradient(135
deg, var(--primary), var(--primary - hover));
box - shadow: var(--shadow - primary);
color: var(--text);
}

.pay - btn: disabled
{
background: linear - gradient(135
deg, var(--primary), var(--primary - hover));
color: var(--text);
box - shadow: var(--shadow - primary);
opacity: .72;
}

.pay - btn.expired: disabled
{
background: var(--danger - soft);
color: var(--danger - light);
box - shadow: none;
opacity: 1;
}

.payment - cancel - btn
{
background: var(--danger - soft);
border: 1
px
solid
var(--danger - border);
color: var(--danger - light);
}

.payment - cancel - btn: disabled
{
opacity: .65;
}

.payment - loading - overlay
{
position: fixed;
inset: 0;
z - index: 95;
display: none;
align - items: center;
justify - content: center;
padding: 24
px;
background: var(--overlay - soft);
backdrop - filter: blur(10
px);
}

.payment - loading - overlay.show
{
display: flex;
}

.payment - loading - box
{
width: min(320
px, 100 %);
border - radius: 22
px;
border: 1
px
solid
var(--line - soft);
background: linear - gradient(180
deg, var(--card), var(--card - 2));
box - shadow: var(--shadow);
padding: 24
px
20
px;
text - align: center;
}

.payment - loading - spinner
{
width: 42
px;
height: 42
px;
margin: 0
auto
14
px;
border - radius: 50 %;
border: 3
px
solid
var(--line - soft);
border - top - color: var(--primary);
animation: spin
.8
s
linear
infinite;
}

.payment - loading - title
{
font - size: 16
px;
font - weight: 800;
color: var(--text);
}

@keyframes


spin
{
to
{
    transform: rotate(360deg);
}
}

/ *press
effect * /
.detail - scroll,
.checkout - scroll
{
/ *max - height: 88
vh; * /
overflow - y: auto;
padding: 12
px
16
px
16
px;
scrollbar - width: none
}

.detail - scroll::-webkit - scrollbar,
.checkout - scroll::-webkit - scrollbar
{
display: none
}

.grabber
{
width: 64
px;
height: 5
px;
border - radius: 999
px;
background: var(--line - soft);
margin: 8
px
auto
14
px
}

.label
{
display: block;
font - size: 13
px;
font - weight: 700;
color: var(--text - soft);
margin - bottom: 8
px
}

.input - wrap
{
position: relative;
background: var(--line - soft);
border: 1
px
solid
var(--line);
border - radius: 14
px;
padding: 11
px
12
px;
margin - top: 10
px;
transition: border - color
.18
s, box - shadow
.18
s
}

.input - wrap: focus - within
{
border - color: var(--primary - border - strong);
box - shadow: 0
0
0
3
px
var(--primary - focus)
}

.input - wrap.error
{
border - color: var(--danger - border - strong);
box - shadow: 0
0
0
3
px
var(--danger - soft)
}

.input
{
width: 100 %;
outline: none;
background: transparent;
border: 0;
color: var(--text);
font - size: 15
px;
line - height: 1.25
}

.input.error
{
border - color: var(--danger - border);
box - shadow: 0
0
0
3
px
var(--danger - soft)
}

.input::placeholder
{
color: var(--text - muted)
}

.username - prefix
{
display: none;
position: absolute;
left: 12
px;
top: 11
px;
color: var(--text);
font - size: 15
px;
line - height: 1.25;
font - weight: 700;
pointer - events: none
}

.input - wrap.username - mode.username - prefix
{
display: block
}

.input - wrap.username - mode.input
{
padding - left: 18
px;
padding - right: 72
px
}

.username - self - btn
{
display: none;
position: absolute;
right: 8
px;
top: 6
px;
min - height: 30
px;
border - radius: 10
px;
padding: 0
9
px;
background: var(--primary - soft);
border: 1
px
solid
var(--primary - border);
color: var(--text - soft);
font - size: 12
px;
font - weight: 800
}

.input - wrap.username - mode.username - self - btn
{
display: block
}

.username - lookup
{
display: none;
margin - top: 9
px;
font - size: 12
px;
color: var(--text - muted)
}

.username - lookup.show
{
display: block
}

.username - lookup.error
{
color: var(--danger - light)
}

.username - preview
{
display: flex;
align - items: center;
gap: 10
px
}

.username - preview
img
{
width: 34
px;
height: 34
px;
border - radius: 50 %;
object - fit: cover;
background: var(--line - soft)
}

.username - preview
strong
{
display: block;
color: var(--text);
font - size: 13
px
}

.username - preview
span
{
color: var(--text - muted);
font - size: 12
px
}

.field - error
{
display: none;
margin - top: 6
px;
font - size: 12
px;
color: var(--danger - light)
}

.input - wrap.error.field - error
{
display: block
}

.package - btn,
.payment - card
{
padding: 14
px
12
px;
border - radius: 18
px;
background: var(--line - soft);
border: 1
px
solid
var(--line);
color: var(--text);
text - align: left
}

.package - btn
strong,
.payment - card
strong
{
display: block;
font - size: 15
px;
margin - bottom: 6
px
}

.price - line
{
margin - top: 12
px;
font - size: 14
px;
color: var(--text - soft)
}

.detailPriceBig,
.checkout - total
strong
{
font - size: 28
px;
letter - spacing: -.03
em
}

.promo - row,
.action - row,
.detail - footer,
.status - actions
{
display: flex;
gap: 12
px;
flex - wrap: wrap
}

.detail - panel
{
display: flex;
flex - direction: column;
}

.detail - scroll
{
flex: 1
1
auto;
min - height: 0;
}

.detail - footer - fixed
{
flex: 0
0
auto;
display: flex;
gap: 12
px;
padding: 12
px
16
px
calc(12
px + env(safe - area - inset - bottom, 0
px));
border - top: 1
px
solid
var(--line - soft);
background: linear - gradient(180
deg, var(--overlay), var(--bg));
backdrop - filter: blur(10
px);
position: relative;
z - index: 5;
}

.promo - row.input - wrap
{
flex: 1;
margin - top: 0
}

.promo - status
{
margin - top: 10
px;
font - size: 12
px;
color: var(--text - muted);
line - height: 1.45
}

.promo - status.success
{
color: var(--success - light)
}

.promo - status.error
{
color: var(--danger - light)
}

.promo - modal
{
max - height: 82
vh;
overflow: hidden;
display: flex;
flex - direction: column;
gap: 12
px
}

.promo - modal - head
{
display: flex;
align - items: center;
justify - content: space - between;
gap: 12
px
}

.promo - modal - title
{
margin: 0;
font - size: 22
px;
font - weight: 900
}

.promo - modal - body
{
overflow - y: auto;
display: grid;
gap: 10
px;
padding - right: 2
px;
scrollbar - width: none
}

.promo - modal - body::-webkit - scrollbar
{
display: none
}

.promo - item
{
display: flex;
align - items: center;
justify - content: space - between;
gap: 12
px;
padding: 12
px;
border - radius: 16
px;
background: var(--line - soft);
border: 1
px
solid
var(--line)
}

.promo - code
{
font - size: 16
px;
font - weight: 900;
letter - spacing: .02
em
}

.promo - meta
{
margin - top: 4
px;
color: var(--text - muted);
font - size: 12
px;
line - height: 1.45
}

.promo - copy - btn
{
min - height: 38
px;
border - radius: 12
px;
padding: 0
12
px;
background: var(--primary - soft);
border: 1
px
solid
var(--primary - border);
color: var(--text);
font - weight: 800
}

.btn - primary,
.btn - secondary
{
min - height: 48
px;
border - radius: 16
px;
padding: 0
18
px;
font - weight: 700;
font - size: 14
px;
color: var(--text)
}

.btn - primary
{
background: linear - gradient(135
deg, var(--primary), var(--primary - hover));
box - shadow: var(--shadow - primary)
}

.btn - primary: disabled,
.btn - secondary: disabled
{
opacity: .55;
box - shadow: none;
cursor: not -allowed
}

.btn - secondary
{
background: var(--line - soft);
border: 1
px
solid
var(--line)
}

.status - modal
{
position: fixed;
left: 50 %;
top: 50 %;
width: calc(100 % - 28
px);
max - width: 520
px;
transform: translate(-50 %, -46 %)
scale(.96);
opacity: 0;
pointer - events: none;
transition: opacity
.28
s
ease, transform
.32
s
var(--ease);
z - index: 80;
padding: 16
px;
border - radius: 28
px
}

.status - modal.show
{
opacity: 1;
pointer - events: auto;
transform: translate(-50 %, -50 %)
scale(1)
}

.status - icon
{
width: 84
px;
height: 84
px;
border - radius: 28
px;
margin: 6
px
auto
16
px;
display: grid;
place - items: center;
font - size: 38
px;
background: linear - gradient(135
deg, var(--primary - soft), rgba(56, 189, 248, .14));
border: 1
px
solid
var(--line - soft)
}

.status - title
{
text - align: center;
font - size: 28
px;
font - weight: 900;
margin: 0
}

.status - text
{
text - align: center;
font - size: 14
px;
margin: 10
px
0
10
px
}

.status - card
{
padding: 14
px;
margin: 16
px
0
16
px;
border - radius: 20
px
}

.loading - dots
{
display: inline - flex;
align - items: center;
gap: 6
px;
margin - top: 14
px;
justify - content: center;
width: 100 %
}

.loading - dots
span
{
width: 10
px;
height: 10
px;
border - radius: 50 %;
background: rgba(160, 171, 255, .85);
animation: pulseDot
1
s
infinite
ease - in -out
}

.loading - dots
span: nth - child(2)
{
animation - delay: .12
s
}

.loading - dots
span: nth - child(3)
{
animation - delay: .24
s
}

@keyframes


pulseDot
{

0 %,
80 %,
100 % {
    transform: scale(.7);
opacity: .45
}

40 % {
    transform: scale(1);
opacity: 1
}
}

# toastContainer {
position: fixed;
bottom: calc(90
px + env(safe - area - inset - bottom));
left: 50 %;
transform: translateX(-50 %);
width: calc(100 % - 32
px);
max - width: 420
px;

display: flex;
flex - direction: column - reverse;
/ *yangi
tepaga
chiqadi * /
gap: 10
px;

z - index: 999;
}

.toast - item
{
    background: rgba(14, 28, 52, .95);
border: 1
px
solid
var(--line - soft);
padding: 14
px
16
px;
border - radius: 16
px;
color: var(--text);
font - weight: 700;
box - shadow: var(--shadow - soft);

opacity: 0;
transform: translateY(20
px) scale(.95);
transition: .25
s
ease;
}

.toast - item.show
{
    opacity: 1;
transform: translateY(0)
scale(1);
}

.toast - item.hide
{
    opacity: 0;
transform: translateY(10
px) scale(.9);
}

@media(max - width

:360
px) {

    .game - strip,
.products,
.package - list,
.payment - grid,
.detail - info - grid,
.topup - amounts
{
grid - template - columns: 1
fr
}

.detail - footer,
.status - actions,
.promo - row
{
flex - direction: column
}
}

@media(min - width

: 560
px) {

    .game - strip,
.products,
.payment - grid,
.topup - amounts
{
grid - template - columns: repeat(3, minmax(0, 1
fr));
}

.package - list
{
grid - template - columns: repeat(4, minmax(0, 1
fr));
}
}
< / style >
    < / head >

        < body >
        < div


class ="app-shell" >

< div


class ="ambient" > < / div >

< header


class ="topbar" >

< div


class ="brand" >

< div


class ="avatar" >

< img
src = ""
alt = "" >
< / div >
< div >
< div


class ="brand-title" > Asilbek Coder < / div >

< div


class ="brand-subtitle" > Game Service < / div >

< / div >
< / div >
< button


class ="balance-chip" id="balanceChip" >

< !-- < span


class ="coin" > < / span > -->

< span > 0
so
'm</span>
< / button >
< / header >

< main


class ="view-stack" >

< section


class ="page active" data-page="home" >

< div


class ="section" id="bannerSection" >

< div


class ="section-head" >

< h2


class ="section-title" > E'lonlar</h2>

< / div >
< div


class ="banner-slider banner-style-1" >

< button


class ="slider-nav prev" id="bannerPrev" style="display:none" > ‹ < / button >

< div


class ="banner-track" id="bannerTrack" >

< div


class ="banner-slide active"


style = "--banner-image:url('assets/banner3.png');" >
< div


class ="banner-content" >

< strong > Chegirmalar < / strong >
< span > Eng
mashhur
o
'yinlar uchun qulay narxlar</span>
< / div >
< / div >
< div


class ="banner-slide"


style = "--banner-image:url('assets/banner2.png');" >
< div


class ="banner-content" >

< strong > Tezkor
xizmat < / strong >
< span > Buyurtmalarni
bir
daqiqada
topshirish < / span >
< / div >
< / div >
< div


class ="banner-slide"


style = "--banner-image:url('assets/banner02.png');" >
< div


class ="banner-content" >

< strong > 24 / 7
Admin < / strong >
< span > Har
kuni
doimiy
faol
xizmat < / span >
< / div >
< / div >
< / div >
< button


class ="slider-nav next" id="bannerNext" style="display:none" > › < / button >

< / div >
< div


class ="banner-dots" id="bannerDots" >

< button


class ="banner-dot active" data-slide="0" > < / button >

< button


class ="banner-dot" data-slide="1" > < / button >

< button


class ="banner-dot" data-slide="2" > < / button >

< / div >
< / div >

< div


class ="section" >

< div


class ="section-head" >

< h2


class ="section-title" > Kategoriyalar < / h2 >

< / div >
< div


class ="categories" id="categoryChips" >

< button


class ="chip active" data-filter="all" > Barchasi < / button >

< button


class ="chip" data-filter="games" > O'yinlar</button>

< button


class ="chip" data-filter="premium" > Premium < / button >

< button


class ="chip" data-filter="stars" > Stars < / button >

< !--
pass
prime < button


class ="chip" data-filter="voucher" > Voucher < / button > -->

< / div >
< / div >

< div


class ="section" >

< div


class ="section-head" >

< h2


class ="section-title" > Mashhur o'yinlar</h2>

< / div >
< div


class ="products" >

< article


class ="product-card" data-open-detail="mlbb" data-category="games" >

< div


class ="product-thumb" > < img src="assets/mlbb.png" alt="MLBB" / > < / div >

< div


class ="product-title" > MLBB < / div >

< div


class ="price" > 20 000 < small > UZS < / small > < / div >

< div


class ="meta-row" > < span class ="qty-tag" > Tez yetkaziladi < / span > < button class ="icon-btn" > → < / button >

< / div >
< / article >
< article


class ="product-card" data-open-detail="freefire" data-category="games" >

< div


class ="product-thumb" > < img src="assets/freefire.png" alt="Free Fire" / > < / div >

< div


class ="product-title" > Free Fire < / div >

< div


class ="price" > 42 000 < small > UZS < / small > < / div >

< div


class ="meta-row" > < span class ="qty-tag" > Mashhur paket < / span > < button class ="icon-btn" > → < / button > < / div >

< / article >
< article


class ="product-card" data-open-detail="premium" data-category="premium" >

< div


class ="product-thumb" > < img src="assets/premium.png" alt="PUBG" / > < / div >

< div


class ="product-title" > Premium < / div >

< div


class ="price" > 45 000 < small > UZS < / small > < / div >

< div


class ="meta-row" > < span class ="qty-tag" > Maxsus < / span > < button class ="icon-btn" > → < / button > < / div >

< / article >
< article


class ="product-card" data-open-detail="stars" data-category="stars" >

< div


class ="product-thumb" > < img src="assets/stars.png" alt="Valorant" / > < / div >

< div


class ="product-title" > 50 stars < / div >

< div


class ="price" > 10 000 < small > UZS < / small > < / div >

< div


class ="meta-row" > < span class ="qty-tag" > Arzon < / span > < button class ="icon-btn" > → < / button > < / div >

< / article >
< / div >
< / div >
< div


class ="section none" >

< div


class ="section-head" >

< h2


class ="section-title" > Tanlangan mahsulotlar < / h2 >

< button


class ="link-btn" id="openSelectedGame" > Ochish < / button >

< / div >
< div


class ="game-strip" >

< article


class ="game-card is-selected" data-game="mlbb" data-category="pass topup" >

< div


class ="game-cover"


style = "background:linear-gradient(160deg, rgba(45,226,196,.28), rgba(59,97,255,.18));" >
< div


class ="game-logo" > < img src="assets/mlbb.png" alt="Mobile Legends" / > < / div >

< div


class ="floating-badge" > Tezkor < / div >

< / div >
< div


class ="game-title" > Mobile Legends < / div >

< div


class ="game-meta" > < span class ="pill success" > ● Aktiv < / span > < span class ="pill" > Diamond / Pass < / span >

< / div >
< / article >

< article


class ="game-card" data-game="pubg" data-category="topup" >

< div


class ="game-cover"


style = "background:linear-gradient(160deg, rgba(47,107,255,.20), rgba(56,189,248,.10));" >
< div


class ="game-logo" > < img src="assets/pubg.png" alt="PUBG Mobile" / > < / div >

< div


class ="floating-badge" > Trend < / div >

< / div >
< div


class ="game-title" > PUBG Mobile < / div >

< div


class ="game-meta" > < span class ="pill success" > ● Aktiv < / span > < span class ="pill" > UC < / span > < / div >

< / article >

< article


class ="game-card" data-game="freefire" data-category="topup voucher" >

< div


class ="game-cover"


style = "background:linear-gradient(160deg, var(--primary-soft), rgba(56,189,248,.12));" >
< div


class ="game-logo" > < img src="assets/freefire.png" alt="Free Fire" / > < / div >

< div


class ="floating-badge" > Mashhur < / div >

< / div >
< div


class ="game-title" > Free Fire < / div >

< div


class ="game-meta" > < span class ="pill success" > ● Aktiv < / span > < span class ="pill" > Diamond < / span > < / div >

< / article >

< article


class ="game-card" data-game="valorant" data-category="voucher prime" >

< div


class ="game-cover"


style = "background:linear-gradient(160deg, rgba(47,107,255,.22), rgba(34,53,98,.24));" >
< div


class ="game-logo" > < img src="assets/valorant.png" alt="Valorant" / > < / div >

< div


class ="floating-badge" > Yangi < / div >

< / div >
< div


class ="game-title" > Valorant Points < / div >

< div


class ="game-meta" > < span class ="pill success" > ● Aktiv < / span > < span class ="pill" > VP < / span > < / div >

< / article >
< / div >
< / div >

< / section >

< section


class ="page" data-page="cart" >

< div


class ="section-head" >

< h2


class ="section-title" > Savat < / h2 > < button class ="link-btn" id="clearCart" > Tozalash < / button >

< / div >
< div


class ="cart-list" id="cartList" > < / div >

< div


class ="summary-box" >

< div


class ="summary-row" > < span > Mahsulotlar < / span > < span id="summaryCount" > 0 ta < / span > < / div >

< div


class ="summary-row" > < span > Komissiya < / span > < span > 0 % < / span > < / div >

< div


class ="summary-row" > < span > Promokod < / span > < span id="summaryPromo" > — < / span > < / div >

< div


class ="summary-row" > < span > Jami < / span > < strong id="summaryTotal" > 0 UZS < / strong > < / div >

< div


class ="action-row" style="margin-top:14px;" >

< button


class ="btn-secondary" style="min-width:110px;" id="openPromoHint" > Promokod < / button >

< button


class ="btn-primary" style="flex:1;" id="openCheckoutBtn" > Sotib olish < / button >

< / div >
< / div >
< / section >

< section


class ="page" data-page="balance" >

< div


class ="section-head" >

< h2


class ="section-title none" > Balans < / h2 >

< button


class ="link-btn none" id="goProfileBtn" > Profil < / button >

< / div >
< div


class ="summary-box none" style="padding:18px;" >

< div


class ="muted" > Joriy balans < / div >

< div
style = "font-size:34px;font-weight:900;letter-spacing:-.03em;margin-top:6px;" > 0
UZS < / div >
< div


class ="helper-text" > Balansni to'ldirib, buyurtmalarni tezroq rasmiylashtiring.</div>

< / div >

< div


class ="section none" >

< div


class ="section-head" >

< h2


class ="section-title" > Karta tanlash < / h2 >

< / div >
< div


class ="payment-grid balance-methods" >

< button


class ="payment-card active" data-balance-method="uzcard" > < strong > Uzcard < / strong > < span > Faol karta


orqali < / span > < / button >
< button


class ="payment-card" data-balance-method="humo" > < strong > Humo < / strong > < span > Faol karta


orqali < / span > < / button >
< button


class ="payment-card" data-balance-method="click" > < strong > Click < / strong > < span > Tezkor onlayn


to
'lov</span></button>
< button


class ="payment-card" data-balance-method="payme" > < strong > Payme < / strong > < span > Mobil to'lov


usuli < / span > < / button >
< / div >
< / div >

< div


class ="section" >

< div


class ="section-head" >

< h2


class ="section-title" > Miqdor tanlash < / h2 >

< / div >

< !-- preset -->
< div


class ="topup-amounts" >

< button


class ="topup-chip active" data-amount="50000" > 50 000 < / button >

< button


class ="topup-chip" data-amount="100000" > 100 000 < / button >

< button


class ="topup-chip" data-amount="200000" > 200 000 < / button >

< button


class ="topup-chip" data-amount="500000" > 500 000 < / button >

< / div >

< !-- custom
input -->
< div


class ="input-wrap" id="customTopupWrap" >

< input


class ="input" id="customTopupInput" type="number" inputmode="numeric" min="10000" max="100000000" maxlength="9"


placeholder = "Boshqa summa" / >
< div


class ="field-error" id="customTopupError" > Minimal summa 10 000 so‘m < / div >

< / div >

< !-- result -->
< div


class ="summary-box" style="margin-top:12px;" >

< div


class ="muted" > Tanlangan summa < / div >

< strong
id = "topupAmountText" > 50
000
UZS < / strong >
< / div >
< / div >

< div


class ="detail-footer section" >

< button


class ="btn-secondary" id="balanceCancelBtn" style="flex:1;" > Bekor qilish < / button >

< button


class ="btn-primary" id="balanceTopupBtn" style="flex:1;" > Balansni to'ldirish</button>

< / div >
< / section >

< section


class ="page" data-page="profile" >

< div


class ="profile-hero" >

< div


class ="profile-avatar" >

< img
src = ""
alt = "" >
< / div >
< div


class ="profile-name" > Asilbek Coder < / div >

< div


class ="profile-id" > ID: 5819317484 <

/ div >
< / div >
< div


class ="profile-list section" >

< article


class ="profile-card actionable referral-card" id="referralsCard" >

< div


class ="profile-left" >

< div


class ="profile-circle" > 👥 < / div >

< div >
< div


class ="profile-name-row" > Referallar < / div >

< div


class ="profile-desc" id="referralsCardDesc" > Taklif qilganlar: 0


ta < / div >
< / div >
< / div >
< div


class ="value" id="referralsCardValue" > 0 so‘m < / div >

< / article >
< article


class ="profile-card actionable" id="discountsCard" >

< div


class ="profile-left" >

< div


class ="profile-circle" > 🎁 < / div >

< div >
< div


class ="profile-name-row" > Chegirmalar < / div >

< div


class ="profile-desc" > Faol promokod va bonuslar < / div >

< / div >
< / div >
< div


class ="value" id="discountsCount" > 0 ta < / div >

< / article >
< !-- < article


class ="profile-card" > < div class ="profile-left" > < div class ="profile-circle" > 🌐 < / div > < div > < div class ="profile-name-row" > Til < / div > < div class ="profile-desc" > Interfeys tili < / div > < / div > < / div > < div class ="value" > O'zbek</div></article> -->

< article


class ="profile-card actionable" id="adminSupportCard" >

< div


class ="profile-left" >

< div


class ="profile-circle" > 👤 < / div >

< div >
< div


class ="profile-name-row" > Admin < / div >

< div


class ="profile-desc" > 24 / 7 yordam markazi < / div >

< / div >
< / div >
< div


class ="value" id="adminSupportValue" > Online < / div >

< / article >
< / div >

< div


class ="section" >

< div


class ="section-head" >

< h2


class ="section-title" > Tarix < / h2 >

< / div >

< !-- Tabs -->
< div


class ="history-tabs" >

< button


class ="history-tab active" data-tab="orders" > Buyurtmalar < / button >

< button


class ="history-tab" data-tab="payments" > To‘lovlar < / button >

< / div >

< !-- Filter -->
< div


class ="history-filters" >

< button


class ="filter-chip active" data-status="all" > Barchasi < / button >

< button


class ="filter-chip" data-status="pending" > Kutilmoqda < / button >

< button


class ="filter-chip" data-status="success" > Muvaffaqiyatli < / button >

< button


class ="filter-chip" data-status="cancel" > Bekor qilingan < / button >

< button


class ="filter-chip" data-status="expired" > Muddati tugagan < / button >

< / div >

< !-- List -->
< div
id = "historyList"


class ="history-list" >

< !-- JS
orqali
chiqadi -->
< / div >
< / div >
< / section >
< / main >

< nav


class ="bottom-nav" >

< div


class ="nav-grid" >

< button


class ="nav-item active" data-target="home" > < ion-icon class ="icon"


name = "home-outline" > < / ion - icon > < span > Asosiy < / span > < / button >
< button


class ="nav-item" data-target="cart" > < ion-icon class ="icon"


name = "cart-outline" > < / ion - icon > < span > Savat < / span > < / button >
< button


class ="nav-item" data-target="balance" > < ion-icon class ="icon"


name = "card-outline" > < / ion - icon > < span > Balans < / span > < / button >
< button


class ="nav-item" data-target="profile" > < ion-icon class ="icon"


name = "person-outline" > < / ion - icon > < span > Profil < / span > < / button >
< / div >
< / nav >

< div


class ="checkout-panel-backdrop" id="checkoutBackdrop" > < / div >

< div


class ="checkout-panel" id="checkoutPanel" >

< div


class ="checkout-scroll" >

< div


class ="grabber" > < / div >

< div


class ="detail-card none" >

< label


class ="label" > To'lov usuli</label>

< div


class ="payment-grid" id="paymentGrid" >

< button


class ="payment-card active" data-payment="uzcard" > < strong > Uzcard < / strong > < span > Karta orqali


to
'lov</span></button>
< button


class ="payment-card" data-payment="humo" > < strong > Humo < / strong > < span > Milliy to'lov</span></button>

< button


class ="payment-card" data-payment="balance" > < strong > Balans < / strong > < span > Ichki


hisobdan < / span > < / button >
< button


class ="payment-card" data-payment="click" > < strong > Click < / strong > < span > Tezkor to'lov</span></button>

< / div >
< / div >

< div


class ="detail-card" >

< label


class ="label" > Buyurtma xulosasi < / label >

< div


class ="summary-row" > < span > Mahsulotlar < / span > < span id="checkoutItemsCount" > 0 ta < / span > < / div >

< div


class ="summary-row" > < span > Jami summa < / span > < span id="checkoutSubtotal" > 0 UZS < / span > < / div >

< div


class ="summary-row" > < span > Chegirma < / span > < span id="checkoutDiscount" > 0 UZS < / span > < / div >

< div


class ="summary-row" > < span > Komissiya < / span > < span > 0 UZS < / span > < / div >

< div


class ="checkout-total" >

< div >
< div


class ="tiny-note" > To'lanadigan summa</div>

< strong
id = "checkoutGrandTotal" > 0
UZS < / strong >
< / div >
< span


class ="pill success" id="checkoutPaymentName" > Uzcard < / span >

< / div >
< / div >

< div


class ="detail-card" >

< label


class ="label" > Promokod < / label >

< div


class ="promo-row" >

< div


class ="input-wrap" > < input class ="input" id="promoInput" placeholder="Kod kiriting" / > < / div >

< button


class ="btn-secondary" id="applyPromoBtn" > Qo‘llash < / button >

< button


class ="btn-secondary none" id="clearPromoBtn" type="button" > Bekor qilish < / button >

< / div >
< div


class ="promo-status" id="promoStatus" > Promo kod checkout buyurtmasiga qo‘llanadi.< / div >

< / div >

< div


class ="detail-footer" >

< button


class ="btn-secondary" id="closeCheckoutBtn" style="flex:1;" > Bekor qilish < / button >

< button


class ="btn-primary" id="confirmCheckoutBtn" style="flex:1;" > To'lovga o'tish < / button >

< / div >
< / div >
< / div >

< div


class ="detail-panel-backdrop" id="detailBackdrop" > < / div >

< div


class ="detail-panel" id="detailPanel" >

< div


class ="detail-scroll" >

< div


class ="grabber" > < / div >

< div


class ="detail-game-header" >

< div


class ="detail-game-icon-wrap" >

< img
src = "assets/mlbb.png"
alt = "Game"
id = "detailIconImg"


class ="detail-game-icon" / >

< / div >

< div


class ="detail-game-info" >

< div
id = "detailTitle"


class ="detail-game-name" > Mobile Legends < / div >

< div
id = "detailSubtitle"


class ="detail-game-desc" > Diamond, Weekly Pass va Twilight Pass xizmatlari.< / div >

< / div >

< span


class ="pill success" > ● Aktiv < / span >

< / div >

< div


class ="input-wrap" id="playerIdWrap" >

< span


class ="username-prefix" > @ < / span >

< input


class ="input" id="playerIdInput" type="number" inputmode="numeric" maxlength="32" placeholder="O'yinchi ID" / >

< button


class ="username-self-btn" id="usernameSelfBtn" type="button" > O‘zimga < / button >

< div


class ="field-error" id="playerIdError" > O'yinchi ID kiriting.</div>

< div


class ="username-lookup" id="usernameLookup" > < / div >

< / div >

< div


class ="input-wrap" id="serverIdCard" style="display:none;" >

< input


class ="input" id="serverIdInput" type="number" inputmode="numeric" maxlength="32" placeholder="Server ID" / >

< div


class ="field-error" id="serverIdError" > Server ID kiriting.< / div >

< / div >

< div


class ="input-wrap" id="starsAmountWrap" style="display:none;" >

< input


class ="input" id="starsAmountInput" type="number" inputmode="numeric" min="50" maxlength="10"


placeholder = "Stars miqdori" / >
< div


class ="field-error" id="starsAmountError" > Kamida 50 stars kiriting.< / div >

< / div >

< div


class ="detail-card" >

< label


class ="label" > Paketni tanlang < / label >

< div


class ="package-list" id="packageList" > < / div >

< div


class ="price-line" > < span > Tanlangan summa < / span > < strong class ="detailPriceBig" id="detailPrice" > 20 000


UZS < / strong > < / div >
< / div >

< div


class ="detail-card none" >

< label


class ="label" > Qisqacha ma'lumot</label>

< div


class ="detail-info-grid" >

< div


class ="info-box" > < strong id="infoDelivery" > 1-5 min < / strong > < span > Yetkazish < / span > < / div >

< div


class ="info-box" > < strong > 0 % < / strong > < span > Komissiya < / span > < / div >

< div


class ="info-box" > < strong id="infoType" > Pass < / strong > < span > Tur < / span > < / div >

< / div >
< / div >
< / div >

< div


class ="detail-footer-fixed" >

< button


class ="btn-secondary" id="closeDetail" style="flex:1;" > Bekor qilish < / button >

< button


class ="btn-primary" id="addToCartBtn" style="flex:1;" > Savatga qo'shish</button>

< / div >
< / div >

< div


class ="payment-modal" id="paymentModal" >

< div


class ="payment-container" >

< div


class ="payment-scroll" >

< div


class ="payment-header" >

< button


class ="payment-close-btn" id="closePayment" type="button" aria-label="Yopish" >

< ion - icon
name = "chevron-back-outline" > < / ion - icon >
< / button >
< div


class ="payment-title" >

< h3 > Balans
to‘ldirish < / h3 >
< span > Game
Service
to‘lov
oynasi < / span >
< / div >
< div


class ="payment-status-pill" id="paymentStatusPill" > Kutilmoqda < / div >

< / div >

< div


class ="payment-hero" >

< div


class ="payment-amount-card" >

< div


class ="payment-amount-label" > To‘lash kerak < / div >

< div


class ="payment-amount-row" >

< strong
id = "paymentAmount" > 0
UZS < / strong >
< button


class ="payment-copy-btn" id="copyAmount" type="button" aria-label="Summani nusxalash" >

< ion - icon
name = "copy-outline" > < / ion - icon >
< / button >
< / div >
< div


class ="payment-amount-subtitle" id="paymentAmountSubtitle" > Summani aynan yuboring < / div >

< / div >

< div


class ="payment-timer-card" id="paymentTimerCard" >

< div


class ="payment-timer-top" >

< span > To‘lov
muddati < / span >
< strong
id = "timer" > 05:00 < / strong >
< / div >
< div


class ="payment-progress" >

< div


class ="payment-progress-fill" id="paymentProgressFill" > < / div >

< / div >
< / div >
< / div >

< div


class ="payment-card-slider" id="cardSlider" >

< div


class ="payment-section-title" >

< span > To‘lov
kartalari < / span >
< span


class ="payment-card-count" id="paymentCardCount" > 0 ta < / span >

< / div >
< div


class ="card-track" > < / div >

< div


class ="card-dots" id="cardDots" > < / div >

< / div >

< div


class ="payment-info-card" >

< div


class ="payment-step" > < span > 1 < / span > < strong > Summani yuboring < / strong > < / div >

< div


class ="payment-step" > < span > 2 < / span > < strong > “To‘lov qildim” bosing < / strong > < / div >

< div


class ="payment-step" > < span > 3 < / span > < strong > Admin tasdiqlaydi < / strong > < / div >

< / div >

< / div >

< div


class ="payment-footer" >

< div


class ="payment-footer-actions" >

< button


class ="payment-cancel-btn" id="cancelPaymentBtn" type="button" > Bekor qilish < / button >

< button


class ="pay-btn" id="paidBtn" > To'lov qildim</button>

< / div >
< / div >

< / div >
< / div >

< div


class ="payment-loading-overlay" id="paymentLoadingOverlay" aria-live="polite" >

< div


class ="payment-loading-box" >

< div


class ="payment-loading-spinner" > < / div >

< div


class ="payment-loading-title" > To‘lov sahifasi yuklanmoqda < / div >

< div


class ="loading-dots" > < span > < / span > < span > < / span > < span > < / span > < / div >

< / div >
< / div >

< div


class ="overlay-backdrop" id="statusBackdrop" > < / div >

< div


class ="overlay-backdrop" id="maintenanceBackdrop" > < / div >

< div


class ="status-modal" id="maintenanceModal" >

< div


class ="status-icon" > 🛠 < / div >

< h3


class ="status-title" > Texnik ishlar < / h3 >

< p


class ="status-text" > Texnik ishlar olib borilmoqda < / p >

< / div >

< div


class ="overlay-backdrop" id="discountsBackdrop" > < / div >

< div


class ="status-modal promo-modal" id="discountsModal" >

< div


class ="promo-modal-head" >

< h3


class ="promo-modal-title" > Chegirmalar < / h3 >

< button


class ="icon-btn" id="closeDiscountsModal" type="button" aria-label="Yopish" >

< ion - icon
name = "close-outline" > < / ion - icon >
< / button >
< / div >
< div


class ="history-tabs" >

< button


class ="history-tab active" data-promo-tab="available" > Mavjud < / button >

< button


class ="history-tab" data-promo-tab="used" > Ishlatilgan < / button >

< / div >
< div


class ="promo-modal-body" id="discountsList" > < / div >

< / div >

< div


class ="overlay-backdrop" id="referralsBackdrop" > < / div >

< div


class ="status-modal referral-modal" id="referralsModal" >

< div


class ="promo-modal-head" >

< h3


class ="promo-modal-title" > 👥 Referal tizimi < / h3 >

< button


class ="icon-btn" id="closeReferralsModal" type="button" aria-label="Yopish" >

< ion - icon
name = "close-outline" > < / ion - icon >
< / button >
< / div >
< div


class ="referral-stats" >

< div


class ="referral-stat" > < span class ="muted" > Taklif qilganlar < / span > < strong id="referralTotalUsers" > 0 ta < / strong > < / div >

< div


class ="referral-stat" > < span class ="muted" > Bonus daromad < / span > < strong id="referralTotalEarned" > 0 UZS < / strong > < / div >

< / div >
< div


class ="referral-link-box" >

< div


class ="muted" > Referal link < / div >

< div


class ="referral-link" id="referralLinkText" > Yuklanmoqda...< / div >

< / div >
< div


class ="referral-actions" >

< button


class ="btn-secondary" id="copyReferralLink" type="button" > 📋 Nusxalash < / button >

< button


class ="btn-primary" id="shareReferralLink" type="button" > 📤 Ulashish < / button >

< / div >
< div


class ="label" style="margin:4px 0 0;" > Oxirgi referallar < / div >

< div


class ="referral-list" id="referralRecentList" > < / div >

< / div >

< div


class ="status-modal" id="loadingModal" >

< div


class ="status-icon" > ⏳ < / div >

< h3


class ="status-title" > To'lov tayyorlanmoqda</h3>

< p


class ="status-text" > Buyurtma tekshirilmoqda va payment sahifasi uchun ma'lumotlar tayyorlanmoqda.</p>

< div


class ="loading-dots" > < span > < / span > < span > < / span > < span > < / span > < / div >

< div


class ="status-card" >

< div


class ="status-row" > < span > Holat:<

    / span > < strong > Jarayonda < / strong > < / div >
< div


class ="status-row" > < span > Taxminiy vaqt:<

    / span > < strong > 2 - 5
soniya < / strong > < / div >
< / div >
< / div >

< div


class ="status-modal" id="successModal" >

< div


class ="status-icon" > ✅ < / div >

< h3


class ="status-title" > Buyurtma yaratildi < / h3 >

< p


class ="status-text" > Buyurtma muvaffaqiyatli yaratildi va adminga yuborildi.< / p >

< div


class ="status-card" >

< div


class ="status-row" > < span > Buyurtma:<

    / span > < strong
id = "successOrderId" >  # GS-1205</strong></div>
< div


class ="status-row" > < span > Holat:<

    / span > < strong > Kutilmoqda < / strong > < / div >
< div


class ="status-row" > < span > Summa:<

    / span > < strong
id = "successAmount" > 0
UZS < / strong > < / div >
< / div >
< div


class ="status-actions" >

< button


class ="btn-secondary" id="closeSuccessBtn" > Yopish < / button >

< button


class ="btn-primary" id="successProfileBtn" > Profilga o'tish</button>

< / div >
< / div >

< div


class ="status-modal" id="cancelModal" >

< div


class ="status-icon" > ⚠️ < / div >

< h3


class ="status-title" > Checkout bekor qilinsinmi? < / h3 >

< p


class ="status-text" > Hozirgi promokod va tanlangan to'lov usuli saqlanadi, lekin checkout oynasi yopiladi.</p>

< div


class ="status-actions" >

< button


class ="btn-secondary" id="cancelDismissBtn" > Orqaga < / button >

< button


class ="btn-primary" id="cancelConfirmBtn" > Ha, yopish < / button >

< / div >
< / div >

< div


class ="toast" id="toastContainer" > < / div >

< / div >

< script >
// Security: bot
token, DB
password and card
list
are
never
stored in JS;
user
requests
send
Telegram
initData
to
PHP
for verification.
    // TODO
    MVPdan
    keyin: move
    this
    script
    into
    versioned
    assets and add
    richer
    loading / error
    states.
const
tg = (window.Telegram & & window.Telegram.WebApp) ? window.Telegram.WebApp: {
    initData: '',
    initDataUnsafe: {},
    platform: 'web',
    setHeaderColor() {},
    setBackgroundColor() {},
    setBottomBarColor() {},
    requestFullscreen() {},
    onEvent() {},
    BackButton: {show() {}, hide()
{}}
};
tg.setHeaderColor = tg.setHeaderColor | | function()
{};
tg.setBackgroundColor = tg.setBackgroundColor | | function()
{};
tg.setBottomBarColor = tg.setBottomBarColor | | function()
{};
tg.requestFullscreen = tg.requestFullscreen | | function()
{};
tg.onEvent = tg.onEvent | | function()
{};
tg.BackButton = tg.BackButton | | {show()
{}, hide()
{}};
const
tgInitData = tg.initData | | '';
const
hasTelegramAuth = tgInitData.length > 0;
const
tgUnsafe = tg.initDataUnsafe | | {};
const
user = tgUnsafe.user | | {id: '', first_name: 'Telegram User', username: '', photo_url: ''};
const
appshell = document.querySelector('.app-shell');
const
cssVars = getComputedStyle(document.documentElement);
const
appBg = cssVars.getPropertyValue('--bg').trim() | | '#061225';
try {tg.setHeaderColor(appBg);} catch (e) {}
try {tg.setBackgroundColor(appBg);} catch (e) {}
try {tg.setBottomBarColor(appBg);} catch (e) {}
// if (tg.platform != 'tdesktop'){
// appshell.style = "margin: 70px 0 0 0;";
//
try {tg.requestFullscreen();} catch(e) {}
//}
const
avatar = document.querySelector('.avatar img');
const
brandTitle = document.querySelector('.brand-title');
const
brandSubtitle = document.querySelector('.brand-subtitle');
const
avatar2 = document.querySelector('.profile-avatar img');
const
profilename = document.querySelector('.profile-name');
const
profileid = document.querySelector('.profile-id');
const
u_name = user.first_name | | 'Telegram User';
const
photo_url = user.photo_url | | '';
profilename.textContent = u_name;
profileid.textContent = user.id;
avatar.src = photo_url;
avatar2.src = photo_url;

const
navItems = [...document.querySelectorAll('.nav-item')];
let
gameCards = [...document.querySelectorAll('.product-card')];
const
categoryChips = [...document.querySelectorAll('#categoryChips .chip')];
let
productCards = [...document.querySelectorAll('[data-open-detail]')];
let
bannerSlides = [...document.querySelectorAll('.banner-slide')];
let
bannerDots = [...document.querySelectorAll('.banner-dot')];
let
bannerData = [];
let
bannerSettings = {animation_style: '1', show_arrows: 1, transition_seconds: 4};
let
bannerCarouselPosition = 0;
let
bannerTransitioning = false;
let
bannerTransitionTimer = null;
let
bannerPendingTargetIndex = null;
let
bannerPendingPosition = null;
let
bannerPointerStartX = 0;
let
bannerPointerStartY = 0;
let
bannerPointerMoved = false;
let
bannerPointerActive = false;
const
BANNER_TRANSITION_MS = 720;
const
BANNER_STYLE_2_GAP = 12;
const
paymentCards = [...document.querySelectorAll('#paymentGrid .payment-card')];
const
balanceMethodCards = [...document.querySelectorAll('[data-balance-method]')];
const
topupChips = [...document.querySelectorAll('.topup-chip')];
// const
toast = document.getElementById('toast');

const
detailBackdrop = document.getElementById('detailBackdrop');
const
detailPanel = document.getElementById('detailPanel');
const
checkoutBackdrop = document.getElementById('checkoutBackdrop');
const
checkoutPanel = document.getElementById('checkoutPanel');
const
statusBackdrop = document.getElementById('statusBackdrop');
const
maintenanceBackdrop = document.getElementById('maintenanceBackdrop');
const
maintenanceModal = document.getElementById('maintenanceModal');
const
loadingModal = document.getElementById('loadingModal');
const
successModal = document.getElementById('successModal');
const
cancelModal = document.getElementById('cancelModal');
const
discountsBackdrop = document.getElementById('discountsBackdrop');
const
discountsModal = document.getElementById('discountsModal');
const
discountsList = document.getElementById('discountsList');
const
discountsCount = document.getElementById('discountsCount');
const
referralsBackdrop = document.getElementById('referralsBackdrop');
const
referralsModal = document.getElementById('referralsModal');
const
referralRecentList = document.getElementById('referralRecentList');

const
packageList = document.getElementById('packageList');
const
playerIdInput = document.getElementById('playerIdInput');
const
serverIdInput = document.getElementById('serverIdInput');
const
serverIdCard = document.getElementById('serverIdCard');
const
playerIdWrap = document.getElementById('playerIdWrap');
const
serverIdError = document.getElementById('serverIdError');
const
playerIdError = document.getElementById('playerIdError');
const
usernameSelfBtn = document.getElementById('usernameSelfBtn');
const
usernameLookup = document.getElementById('usernameLookup');
const
starsAmountWrap = document.getElementById('starsAmountWrap');
const
starsAmountInput = document.getElementById('starsAmountInput');
const
starsAmountError = document.getElementById('starsAmountError');
const
customTopupInput = document.getElementById('customTopupInput');
const
customTopupWrap = document.getElementById('customTopupWrap');
const
customTopupError = document.getElementById('customTopupError');
const
cartList = document.getElementById('cartList');
const
summaryCount = document.getElementById('summaryCount');
const
summaryTotal = document.getElementById('summaryTotal');
const
addToCartBtn = document.getElementById('addToCartBtn');

let
currentPage = 'home';
let
headerPage = 'home';
let
isAnimating = false;
let
activeGame = 'mlbb';
let
selectedPackageIndex = 0;
let
selectedPayment = 'uzcard';
let
appliedDiscount = 0;
let
appliedPromo = null;
let
lastGrandTotal = 0;
let
bannerIndex = 0;
let
bannerTimer = null;
let
selectedTopupAmount = 50000;
let
currentUserBalance = 0;
let
pendingPayment = null;
let
paymentTimer = null;
let
paymentStatusTimer = null;
let
paymentCloseTimer = null;
let
currentPaymentId = null;
let
currentPaymentAmount = 0;
let
selectedPaymentCardId = null;
let
orderSubmitting = false;
let
paymentSubmitting = false;
let
paymentCancelSubmitting = false;
let
paymentReviewing = false;
let
activePaymentChecking = false;
let
historyOrdersTimer = null;
let
historyLoaded = false;
let
currentAppSettings = {
maintenance_mode: 0,
is_admin: 0,
maintenance_message: 'Texnik ishlar olib borilmoqda',
history_poll_seconds: 5,
payment_poll_seconds: 3,
min_topup: 10000,
max_topup: 100000000,
payment_expire_minutes: 5
};
let
promoCodesLoaded = false;
let
promoCodesData = {available: [], used: []};
let
activePromoTab = 'available';
let
referralData = {enabled: false, ref_link: '', total_users: 0, total_earned: 0, recent: []};
let
knownReferralEarnings = null;
let
usernameLookupTimer = null;
let
usernameLookupState = {
mode: 'none',
status: 'idle',
username: '',
found: false
};
let
currentUserInfo = {
chat_id: user.id | | '',
first_name: u_name,
username: user.username | | '',
photo_url: photo_url,
balance: 0
};
let
currentBotInfo = {
name: 'Game Service',
username: '',
photo_url: 'assets/bot.png',
admin_support_username: ''
};
let
lastCheckedUsername = '';
let
lastLookupResult = null;

const
cartItems = [
// {icon: 'assets/pubg.png', title: 'PUBG Mobile — 325 UC', subtitle: "O'yinchi ID: kiritilmagan", price: 58000,
    qty: 1},
// {icon: 'assets/mlbb.png', title: 'MLBB — Weekly Pass', subtitle: '1 dona xizmat', price: 20000, qty: 1}
];

let
games = {
mlbb: {
    title: 'Mobile Legends',
    icon: 'assets/mlbb.png',
    subtitle: 'Diamond, Weekly Pass va Twilight Pass xizmatlari.',
    type: 'Pass',
    delivery: '1-3 min',
    banner: 'linear-gradient(135deg, var(--primary-border), rgba(56,189,248,.16))',
    packages: [
        {name: '55 Diamond', price: 10600, note: 'Mini paket'},
        {name: '86 Diamond', price: 17000, note: 'Boshlang‘ich paket'},
        {name: '172 Diamond', price: 33000, note: 'Tezkor top-up'},
        {name: 'Weekly Pass', price: 20000, note: '7 kunlik bonuslar'},
        {name: 'Twilight Pass', price: 149000, note: 'Premium xizmat'},
    ]
},
freefire: {
    title: 'Free Fire',
    icon: 'assets/freefire.png',
    subtitle: 'Diamond va event voucher paketlari.',
    type: 'Voucher',
    delivery: '1-4 min',
    banner: 'linear-gradient(135deg, rgba(47,107,255,.22), rgba(56,189,248,.14))',
    packages: [
        {name: '110 Diamond', price: 10999, note: 'Mini paket'},
        {name: '341 Diamond', price: 33500, note: 'Eng ko‘p tanlangan'},
        {name: '572 Diamond', price: 54000, note: 'Katta bonus'},
        {name: '1166 Diamond', price: 109000, note: 'O‘rta paket'},
        {name: '2398 Diamond', price: 217000, note: 'Katta paket'},
        {name: '6160 Diamond', price: 548000, note: 'Eng katta paket'},
    ]
},
premium: {
    title: 'Telegram Premium',
    icon: 'assets/premium.png',
    subtitle: 'Premium to\'plamlar',
    type: 'Top-up',
    delivery: '1-5 min',
    banner: 'linear-gradient(135deg, rgba(47,107,255,.22), rgba(56,189,248,.12))',
    packages: [
        {name: '1 oylik', price: 45000, note: 'Eng ko‘p tanlangan'},
        {name: '3 oylik', price: 160000, note: 'Mini paket'},
        {name: '6 oylik', price: 230000, note: 'O‘rta paket'},
        {name: '12 oylik', price: 410000, note: 'Katta paket'},
    ]
},
stars: {
    title: 'Telegram Stars',
    icon: 'assets/stars.png',
    subtitle: 'Stars to\'plamlar',
    type: 'Prime',
    delivery: '3-10 min',
    banner: 'linear-gradient(135deg, var(--primary-border), rgba(34,53,98,.30))',
    packages: [
        {name: '50 stars', price: 10000, note: 'Kichik paket'},
        {name: '75 stars', price: 17500, note: 'Kichik paket '},
        {name: '100 stars', price: 20000, note: 'Mashhur tanlov'},
        {name: '150 stars', price: 30000, note: 'Eng ko‘p tanlanadi'},
        {name: '200 stars', price: 40000, note: 'O‘rta paket'},
        {name: '250 stars', price: 50000, note: 'O‘rta paket'},
        {name: '500 stars', price: 100000, note: 'Kattaroq'},
        {name: '1000 stars', price: 200000, note: 'Katta paket'},
        {name: '2500 stars', price: 500000, note: 'Katta paket'},
        {name: '5000 stars', price: 1000000, note: 'Katta paket'},
        {name: '10000 stars', price: 2000000, note: 'Eng katta paket'},
    ]
}
};

function
formatPrice(value)
{
return String(value).replace( /\B(?=(\d{3}) + (?!\d)) / g, ' ') + ' UZS';
}

function
escapeHtml(value)
{
return String(value == null ? '': value).replace( / [ & <> "']/g, ch => ({
                                                           '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#039;'
}[ch]));
}

function
normalizeImagePath(image, fallback='assets/package.png')
{
    const
value = String(image | | '').trim();
if (!value)
return fallback;
if (/ ^ https?:\ / \ // i.test(value)) return value;
if (value.startsWith('/assets/')) return value.slice(1);
if (value.startsWith('assets/')) return value;
return value;
}

function
safeCssImageUrl(image, fallback='assets/banner3.png')
{
return normalizeImagePath(image, fallback).replace( / ['"()\\]/g, ch => encodeURIComponent(ch));
}

function
makeRequestId()
{
    const
randomPart = (window.crypto & & crypto.getRandomValues)
? Array.
from

(crypto.getRandomValues(new Uint32Array(2))).map(n= > n.toString(36)).join('') \
    : Math.random().toString(36).slice(2);
return String(user.id | | 'u') + '-' + Date.now().toString(36) + '-' + randomPart;
}

async function
apiPost(url, payload={}, timeoutMs=12000)
{
const
body = Object.assign({}, payload, {initData: tgInitData});
const
controller = window.AbortController ? new
AbortController(): null;
const
timer = controller ? setTimeout(() = > controller.abort(), timeoutMs): null;
let
res;
try {
const fetchPromise = fetch(url, {
method: 'POST',
cache: 'no-store',
headers: {'Content-Type': 'application/json'},
body: JSON.stringify(body),
signal: controller ? controller.signal: undefined
});
if (controller) {
res = await fetchPromise;
} else {
res = await Promise.race([
fetchPromise,
new Promise((_, reject) = > setTimeout(() = > reject(new Error('request_timeout')), timeoutMs))
]);
}
} catch (err) {
const apiErr = new Error((err & & (err.name == = 'AbortError' | | err.message == = 'request_timeout')) ? 'request_timeout': 'network_error');
apiErr.status = 0;
apiErr.data = {success: false, error: apiErr.message};
console.error('API request failed', {url, error: apiErr.message});
if (typeof showToast == = 'function') showToast('Xatolik yuz berdi');
throw apiErr;
} finally {
if (timer) clearTimeout(timer);
}
let
parseFailed = false;
const
data = await res.json().catch(err= > {
    parseFailed = true;
console.error('API JSON parse failed', {url, status: res.status, error: err & & err.message ? err.message: 'bad_json'});
if (typeof showToast == = 'function') showToast('Xatolik yuz berdi');
return {success: false, error: 'bad_json'};
});
if (!res.ok | | !data.success) {
const err = new Error(data.error | | 'api_error');
err.status = res.status;
err.data = data;
console.error('API response failed', {url, status: res.status, data});
if (!parseFailed & & typeof showToast == = 'function') showToast('Xatolik yuz berdi');
throw err;
}
return data;
}

function
setBalance(value)
{
currentUserBalance = Number(value | | 0);
document.querySelector('#balanceChip span').textContent = formatPrice(currentUserBalance).replace(' UZS', " so'm");
}

function
headerImageSrc(value)
{
return normalizeImagePath(value | | 'assets/bot.png', 'assets/bot.png');
}

function
userHeaderSubtitle(userData)
{
if (userData & & userData.username) return '@' + String(userData.username).replace( / ^ @ + /, '');
const
id = userData & & (userData.chat_id | | userData.id) ? (userData.chat_id | | userData.id): '';
return id ? 'ID: ' + id: '@username yo‘q';
}

function
botHeaderSubtitle(botData)
{
if (botData & & botData.username) return '@' + String(botData.username).replace( / ^ @ + /, '');
return '@username yo‘q';
}

function
updateHeaderForPage(page)
{
if (page) headerPage = page;
const
showBot = headerPage == = 'profile';
const
info = showBot ? currentBotInfo: currentUserInfo;
if (brandTitle) brandTitle.textContent = showBot ? (info.name | | 'Game Service'): (info.first_name | | u_name);
if (brandSubtitle) brandSubtitle.textContent = showBot ? botHeaderSubtitle(info): userHeaderSubtitle(info);
if (avatar) {
avatar.src = headerImageSrc(info.photo_url);
avatar.alt = showBot ? (info.name | | 'Bot'): (info.first_name | | 'User');
}
}

function
updateProfile(userData)
{
if (!userData) return;
const
nextReferralEarnings = Number(userData.ref_total_earned | | 0);
if (knownReferralEarnings !== null & & nextReferralEarnings > knownReferralEarnings) {
showToast('🎁 Siz referral bonus oldingiz: +' + referralMoney(nextReferralEarnings - knownReferralEarnings));
}
knownReferralEarnings = nextReferralEarnings;
currentUserInfo = Object.assign({}, currentUserInfo, userData);
profilename.textContent = userData.first_name | | u_name;
profileid.textContent = 'ID: ' + (userData.chat_id | | user.id);
if (userData.photo_url) {
avatar2.src = userData.photo_url;
}
setBalance(userData.balance);
updateReferralCard({
    total_users: Number(userData.ref_total_users | | 0),
    total_earned: Number(userData.ref_total_earned | | 0)
});
updateHeaderForPage();
}

function
referralMoney(value)
{
return formatPrice(Number(value | | 0)).replace(' UZS', " so‘m");
}

function
updateReferralCard(data)
{
const
users = Number(data & & data.total_users | | 0);
const
earned = Number(data & & data.total_earned | | 0);
const
desc = document.getElementById('referralsCardDesc');
const
value = document.getElementById('referralsCardValue');
if (desc) desc.textContent = 'Taklif qilganlar: ' + users + ' ta';
if (value) value.textContent = referralMoney(earned);
}

function
renderReferralModal()
{
document.getElementById('referralTotalUsers').textContent = Number(referralData.total_users | | 0) + ' ta';
document.getElementById('referralTotalEarned').textContent = formatPrice(Number(referralData.total_earned | | 0));
document.getElementById('referralLinkText').textContent = referralData.ref_link | | 'Bot username sozlanmagan';
updateReferralCard(referralData);
const
list = Array.isArray(referralData.recent) ? referralData.recent: [];
referralRecentList.innerHTML = list.length ? list.map(item= > {
    const
username = item.username ? ' (@' + escapeHtml(item.username) + ')': '';
const
source = item.latest_source == = 'order' ? 'Buyurtma': (item.latest_source ==
                                                        = 'payment' ? 'To‘lov': 'Bonus kutilmoqda');
const
percent = Number(item.latest_percent | | 0);
const
meta = Number(item.earned | | 0) > 0 & & percent > 0 ? source + ' · +' + percent + '%': source;
return ` < div


class ="referral-person" > < span > < b > 👤 ${escapeHtml(item.first_name | | 'User')}${username} < / b > < small > ${escapeHtml(meta)} < / small > < / span > < strong > +${referralMoney(item.earned)} < / strong > < / div > `;

}).join(
    ''): '<div class="history-item" style="text-align:center;color:var(--text-muted);">Hozircha referallar yo‘q</div>';
}

async function
loadReferrals()
{
if (!hasTelegramAuth)
{
    showToast('Telegram orqali oching.');
return;
}
referralRecentList.innerHTML = '<div class="history-item" style="text-align:center;color:var(--text-muted);">Yuklanmoqda...</div>';
try {
const data = await apiPost('api/referrals.php');
referralData = {
enabled: Boolean(data.enabled),
ref_link: data.ref_link | | '',
total_users: Number(data.total_users | | 0),
total_earned: Number(data.total_earned | | 0),
type: data.type | | 'percent',
percent: Number(data.percent | | 0),
fixed_amount: Number(data.fixed_amount | | 0),
recent: Array.isArray(data.recent) ? data.recent: []
};
renderReferralModal();
} catch(err)
{
    referralRecentList.innerHTML = '<div class="history-item" style="text-align:center;color:var(--danger-light);">Referallar yuklanmadi</div>';
}
}

function
openReferralsModal()
{
referralsBackdrop.classList.add('show');
referralsModal.classList.add('show');
loadReferrals();
}

function
closeReferralsModal()
{
referralsBackdrop.classList.remove('show');
referralsModal.classList.remove('show');
}

function
copyReferralLink()
{
if (!referralData.ref_link) {
showToast('Referal link tayyor emas');
return;
}
if (navigator.clipboard & & navigator.clipboard.writeText) {
navigator.clipboard.writeText(referralData.ref_link)
.then(() = > showToast('Referal link nusxalandi'))
.catch(() = > copyReferralLinkFallback());
return;
}
copyReferralLinkFallback();
}

function
copyReferralLinkFallback()
{
    const
input = document.createElement('input');
input.value = referralData.ref_link;
document.body.appendChild(input);
input.select();
const
copied = document.execCommand('copy');
input.remove();
showToast(copied ? 'Referal link nusxalandi': 'Nusxalab bo‘lmadi');
}

function
shareReferralLink()
{
if (!referralData.ref_link)
{
showToast('Referal link tayyor emas');
return;
}
const
text = "🎮 Game Service orqali o‘yinlarga qulay narxda topup qiling!\n\n🎁 Bonus olish uchun link:\n" + referralData.ref_link;
const
url = 'https://t.me/share/url?url=' + encodeURIComponent(referralData.ref_link) + '&text=' + encodeURIComponent(text);
if (tg & & typeof tg.openTelegramLink == = 'function')
tg.openTelegramLink(url);
else if (tg & & typeof tg.openLink == = 'function') tg.openLink(url);
else window.open(url, '_blank');
}

function updateBotInfo(botData) {
if (!botData)
return;
currentBotInfo = Object.assign({}, currentBotInfo, {
    name: botData.name | | currentBotInfo.name,
    username: botData.username | | currentBotInfo.username,
    photo_url: botData.photo_url | | currentBotInfo.photo_url,
    admin_support_username: Object.prototype.hasOwnProperty.call(botData, 'admin_support_username')
? botData.admin_support_username
: currentBotInfo.admin_support_username
});
const
supportValue = document.getElementById('adminSupportValue');
if (supportValue) {
const supportUsername = String(currentBotInfo.admin_support_username | | '').replace( / ^ @ + /, '').trim();
supportValue.textContent = supportUsername ? '@' + supportUsername: 'Sozlanmagan';
}
updateHeaderForPage();
}

function
openAdminSupport()
{
const
username = String(currentBotInfo.admin_support_username | | '').replace( / ^


@+ /

, '').trim();
if (!username) {
showToast('Admin user sozlanmagan');
return;
}
const
url = 'https://t.me/' + encodeURIComponent(username);
if (tg & & typeof tg.openTelegramLink == = 'function')
{
tg.openTelegramLink(url);
} else if (tg & & typeof tg.openLink == = 'function') {
tg.openLink(url);
} else {
window.open(url, '_blank');
}
}

function
updateAppSettings(settings)
{
if (!settings)
return;
currentAppSettings = Object.assign({}, currentAppSettings, settings);
const
minTopup = Math.max(0, Number(currentAppSettings.min_topup | | 10000));
const
maxTopup = Math.max(minTopup, Number(currentAppSettings.max_topup | | 100000000));
currentAppSettings.min_topup = minTopup;
currentAppSettings.max_topup = maxTopup;
customTopupInput.min = String(minTopup);
customTopupInput.max = String(maxTopup);
customTopupInput.maxLength = String(Math.trunc(maxTopup)).length;
const
blocked = Number(currentAppSettings.maintenance_mode | | 0) == = 1 & & Number(currentAppSettings.is_admin | | 0) != = 1;
const
message = currentAppSettings.maintenance_message | | 'Texnik ishlar olib borilmoqda';
const
textEl = maintenanceModal ? maintenanceModal.querySelector('.status-text'): null;
if (textEl) textEl.textContent = message;
maintenanceBackdrop.classList.toggle('show', blocked);
maintenanceModal.classList.toggle('show', blocked);
updateAddToCartAvailability();
}

function
isMaintenanceBlocked()
{
const
blocked = Number(currentAppSettings.maintenance_mode | | 0) == = 1 & & Number(currentAppSettings.is_admin | | 0) != = 1;
if (blocked) {
showToast(currentAppSettings.maintenance_message | | 'Texnik ishlar olib borilmoqda');
}
return blocked;
}

async function
loadUser()
{
if (!hasTelegramAuth) {
showToast('Telegram orqali oching.');
return;
}
try {
const data = await apiPost('api/user.php');
updateProfile(data.user);
updateBotInfo(data.bot);
updateAppSettings(data.settings);
loadMyPromocodes({silent: true});
} catch(err)
{
    console.error('user_load_error', {
        message: err.message,
        status: err.status | | 0,
        data: err.data | | null
    });
showToast('Profil backenddan yuklanmadi.');
}
}

function
promoDateText(value)
{
if (!value) return 'muddatsiz';
return String(value).slice(0, 10);
}

function
updateDiscountsCount()
{
if (discountsCount) discountsCount.textContent = (promoCodesData.available.length | | 0) + ' ta';
}

async function
loadMyPromocodes(options={})
{
if (!hasTelegramAuth) {
if (!options.silent) showToast('Telegram orqali oching.');
return;
}
try {
const data = await apiPost('api/my_promocodes.php');
promoCodesData = {
available: Array.isArray(data.available) ? data.available: [],
used: Array.isArray(data.used) ? data.used: []
};
promoCodesLoaded = true;
updateDiscountsCount();
renderDiscountsList();
} catch(err)
{
    console.error('promocodes_load_error', {
        message: err.message,
        status: err.status | | 0,
        data: err.data | | null
    });
if (!options.silent)
{
    showToast('Chegirmalar yuklanmadi.');
}
}
}

function
renderDiscountsList()
{
if (!discountsList) return;
if (activePromoTab === 'available') {
const list = promoCodesData.available | |[];
if (!list.length) {
discountsList.innerHTML = '<div class="history-item" style="text-align:center;color:var(--text-muted);">Hozircha siz uchun promokod yo‘q</div>';
return;
}
discountsList.innerHTML = list.map(item= > `
< div


class ="promo-item" >

< div >
< div


class ="promo-code" > 🎟 ${escapeHtml(item.code)} < / div >

< div


class ="promo-meta" > ${escapeHtml(item.discount_text | | '')} < / div >

< div


class ="promo-meta" > Muddat: $


    {escapeHtml(promoDateText(item.expires_at))} < / div >
< / div >
< button


class ="promo-copy-btn" type="button" data-copy-promo="${escapeHtml(item.code)}" > Copy < / button >

< / div >
`).join('');
} else {
    const
list = promoCodesData.used | | [];
if (!list.length)
{
discountsList.innerHTML = '<div class="history-item" style="text-align:center;color:var(--text-muted);">Siz hali promokod ishlatmagansiz</div>';
return;
}
discountsList.innerHTML = list.map(item= > `
< div


class ="promo-item" >

< div >
< div


class ="promo-code" > ✅ ${escapeHtml(item.code)} < / div >

< div


class ="promo-meta" > Chegirma: $


    {formatPrice(Number(item.discount_amount | | 0))} < / div >
< div


class ="promo-meta" > Buyurtma: $


    {item.order_id ? ('#' + Number(item.order_id)): '—'} < / div >
< / div >
< / div >
`).join('');
}
discountsList.querySelectorAll('[data-copy-promo]').forEach(btn= > {
btn.onclick = () = > copyPromoCode(btn.dataset.copyPromo | | '');
});
}

function
copyPromoCode(code)
{
if (!code)
return;
if (navigator.clipboard & & navigator.clipboard.writeText) {
navigator.clipboard.writeText(code).then(() = > showToast('Promokod nusxalandi')).catch(() = > showToast('Nusxalab bo‘lmadi'));
return;
}
const
input = document.createElement('input');
input.value = code;
document.body.appendChild(input);
input.select();
document.execCommand('copy');
input.remove();
showToast('Promokod nusxalandi');
}

function
openDiscountsModal()
{
    activePromoTab = 'available';
document.querySelectorAll('[data-promo-tab]').forEach(btn= > btn.classList.toggle('active',
                                                                                  btn.dataset.promoTab == = activePromoTab));
discountsBackdrop.classList.add('show');
discountsModal.classList.add('show');
if (!promoCodesLoaded)
{
discountsList.innerHTML = '<div class="history-item" style="text-align:center;color:var(--text-muted);">Yuklanmoqda...</div>';
loadMyPromocodes();
} else {
renderDiscountsList();
}
}

function
closeDiscountsModal()
{
    discountsBackdrop.classList.remove('show');
discountsModal.classList.remove('show');
}

function
renderHomeProducts(cards)
{
if (!cards | | !cards.length)
return;
const
wrap = document.querySelector('.products');
wrap.innerHTML = cards.map(card= > {
    const
game = games[card.game_key];
const
firstPack = game & & game.packages & & game.packages[0] ? game.packages[0]: null;
const
price = firstPack ? firstPack.price: 0;
const
cardImage = normalizeImagePath(card.image | | (game & & game.icon), 'assets/package.png');
return `
< article


class ="product-card" data-open-detail="${escapeHtml(card.game_key)}" data-category="${escapeHtml(card.category || 'games')}" >

< div


class ="product-thumb" > < img src="${escapeHtml(cardImage)}" alt="${escapeHtml(card.title)}" onerror="this.src='assets/package.png'" / > < / div >

< div


class ="product-title" > ${escapeHtml(card.title)} < / div >

< div


class ="price" > ${formatPrice(price).replace(' UZS', '')} < small > UZS < / small > < / div >

< div


class ="meta-row" > < span class ="qty-tag" > Tez yetkaziladi < / span > < button class ="icon-btn" > → < / button > < / div >

< / article >
`;
}).join('');

gameCards = [...document.querySelectorAll('.product-card')];
productCards = [...document.querySelectorAll('[data-open-detail]')];
bindProductCards();
}

async function
loadProducts()
{
    document.querySelector(
        '.products').innerHTML = '<div class="summary-box" style="grid-column:1/-1;text-align:center;color:var(--text-muted);">Mahsulotlar yuklanmoqda...</div>';
try {
const data = await apiPost('api/products.php');
if (data.success & & data.games & & Object.keys(data.games).length) {
games = data.games;
console.log('loaded_games', games);
renderHomeProducts(data.products);
}
} catch (err) {
console.error('products_load_error', {
message: err.message,
status: err.status | | 0,
data: err.data | | null
});
document.querySelector(
    '.products').innerHTML = '<div class="summary-box" style="grid-column:1/-1;text-align:center;color:var(--text-muted);">Mahsulotlar backenddan yuklanmadi.</div>';
showToast(
    err.message == = 'request_timeout' ? 'Mahsulotlar yuklanishi sekinlashdi.': 'Mahsulotlar backenddan yuklanmadi.');
}
}
function
getPackageImage(gameKey, packName)
{
const
name = packName.toLowerCase();

if (gameKey === 'premium') {
const amount = parseInt(packName.replace( / \D / g, '')) | | 0;
if (amount == 3)
return 'assets/oy3.png';
if (amount == 6) return 'assets/oy6.png';
if (amount == 12) return 'assets/oy12.png';
return 'assets/oy3.png';
}

if (gameKey === 'stars') {
const
amount = parseInt(packName.replace( /\D / g, '')) | | 0;
if (amount > 1) return 'assets/stars2.png';
return 'assets/stars1.png';
}

if (gameKey === 'mlbb') {
if (name.includes('twilight')) return 'assets/o3.png';
if (name.includes('weekly')) return 'assets/o2.png';

const
amount = parseInt(packName.replace( /\D / g, '')) | | 0;
if (amount >= 172) return 'assets/o1.png';
return 'assets/oh.png';
}

if (gameKey === 'freefire') {
if (name.includes('weekly')) return 'assets/freefire-weekly.png';

const
amount = parseInt(packName.replace( /\D / g, '')) | | 0;
if (amount >= 110) return 'assets/a1.png';
if (amount >= 341) return 'assets/a2.png';
if (amount >= 572) return 'assets/a3.png';
if (amount >= 1166) return 'assets/a4.png';
if (amount >= 2398) return 'assets/a5.png';
if (amount >= 6160) return 'assets/a6.png';
return 'assets/a1.png';
}

return 'assets/package.png';
}
const
toastContainer = document.getElementById('toastContainer');

const
MAX_TOASTS = 2;

function
showToast(message)
{

const
currentToasts =
toastContainer.querySelectorAll('.toast-item');

// agar
3
ta
bo
'lsa eng eskisini o'
chir
if (currentToasts.length >= MAX_TOASTS) {

const oldestToast = currentToasts[0];

oldestToast.classList.remove('show');
oldestToast.classList.add('hide');

setTimeout(() = > {
oldestToast.remove();
}, 10);
}

// yangi
toast
const
toast = document.createElement('div');

toast.className = 'toast-item';
toast.textContent = message;

toastContainer.appendChild(toast);

requestAnimationFrame(() = > {
    toast.classList.add('show');
});

// auto
remove
setTimeout(() = > {

    toast.classList.remove('show');
toast.classList.add('hide');

setTimeout(() = > {
    toast.remove();
}, 250);

}, 2500);
}


tg.onEvent("backButtonClicked", function()
{
    closePaymentModal();
});

function
switchPage(nextPage)
{
if (nextPage === currentPage) return true;
if (isAnimating) return false;
const
current = document.querySelector(`.page[data - page = "${currentPage}"]`);
const
next = document.querySelector(`.page[data - page = "${nextPage}"]`);
if (!current | | !next) return false;

isAnimating = true;
current.classList.remove('active');
current.classList.add('exit-left');
next.classList.add('active');

navItems.forEach(item= > item.classList.toggle('active', item.dataset.target == = nextPage));

setTimeout(() = > {
    current.classList.remove('exit-left');
currentPage = nextPage;
isAnimating = false;
}, 420);
return true;
}

async function
checkActivePaymentOnBalanceOpen()
{
if (!hasTelegramAuth | | activePaymentChecking) return;
activePaymentChecking = true;
try {
const activePayment = await apiPost('api/active_payment.php');
const balancePage = document.querySelector('.page[data-page="balance"]');
if (activePayment.active & & balancePage & & balancePage.classList.contains('active')) {
showToast("Avvalgi to‘lovingiz hali faol");
openPaymentModal(activePayment);
}
} catch (err) {
console.error('active_payment_check_failed', {
message: err.message,
status: err.status | | 0,
data: err.data | | null
});
} finally {
    activePaymentChecking = false;
}
}

function
openPage(nextPage)
{
if (!switchPage(nextPage)) return;
updateHeaderForPage(nextPage);
updateHistoryOrdersPolling(nextPage);
if (nextPage === 'balance') {
checkActivePaymentOnBalanceOpen();
}
if (nextPage === 'profile') {
loadUser();
}
}

function
stopBannerRuntime()
{
clearInterval(bannerTimer);
clearTimeout(bannerTransitionTimer);
bannerTimer = null;
bannerTransitionTimer = null;
bannerTransitioning = false;
bannerPendingTargetIndex = null;
bannerPendingPosition = null;
const
track = document.getElementById('bannerTrack');
if (track) track.ontransitionend = null;
}

function
updateBannerArrows()
{
const
showArrows = bannerData.length > 1 & & Number(bannerSettings.show_arrows) == = 1;
const
prevBtn = document.getElementById('bannerPrev');
const
nextBtn = document.getElementById('bannerNext');
prevBtn.style.display = showArrows ? '': 'none';
nextBtn.style.display = showArrows ? '': 'none';
}

function
updateBannerDots()
{
bannerDots.forEach((dot, index) = > dot.classList.toggle('active', index == = bannerIndex));
}

function
clearBannerSlideClasses()
{
bannerSlides.forEach(slide= > {
    slide.classList.remove('active', 'prev', 'next', 'is-entering', 'is-leaving');
const
content = slide.querySelector('.banner-content');
if (content)
{
    content.classList.remove('text-enter');
content.onanimationend = null;
}
});
}

function
updateFadeSlider(targetIndex, initial=false)
{
clearTimeout(bannerTransitionTimer);
bannerTransitionTimer = null;
bannerTransitioning = false;
bannerSlides.forEach(slide= > slide.classList.remove('is-entering', 'is-leaving'));
const
currentSlide = bannerSlides.find(slide= > Number(slide.dataset.bannerIndex) == = bannerIndex);
const
nextSlide = bannerSlides.find(slide= > Number(slide.dataset.bannerIndex) == = targetIndex);
if (!nextSlide) return;
if (initial | | targetIndex === bannerIndex) {
clearBannerSlideClasses();
bannerIndex = targetIndex;
nextSlide.classList.add('active');
updateBannerDots();
return;
}

bannerTransitioning = true;
bannerSlides.forEach(slide= > slide.classList.remove('is-entering', 'is-leaving'));
if (currentSlide) {
currentSlide.classList.remove('active');
currentSlide.classList.add('is-leaving');
}
nextSlide.classList.remove('is-entering');
void
nextSlide.offsetWidth;
nextSlide.classList.add('active', 'is-entering');
bannerIndex = targetIndex;
updateBannerDots();

clearTimeout(bannerTransitionTimer);
bannerTransitionTimer = setTimeout(() = > {
    bannerSlides.forEach(slide= > slide.classList.remove('is-entering', 'is-leaving'));
bannerTransitioning = false;
bannerTransitionTimer = null;
}, BANNER_TRANSITION_MS);
}

function
setInfiniteTrackPosition(position, animate)
{
    const
track = document.getElementById('bannerTrack');
if (!track)
return;
const
slider = document.querySelector('#bannerSection .banner-slider');
const
step = (slider ? slider.clientWidth: 0) + BANNER_STYLE_2_GAP;
track.style.transition = animate
? `transform ${BANNER_TRANSITION_MS}
ms
cubic - bezier(.22, .61, .36, 1)
`
: 'none';
if (animate) void track.offsetWidth;
track.style.transform = `translate3d(-${position * step}
px, 0, 0)`;
}

function
markInfiniteActive()
{
bannerSlides.forEach((slide, index) = > slide.classList.toggle('active', index == = bannerCarouselPosition));
}

function
replayInfiniteTextAnimation()
{
bannerSlides.forEach(slide= > {
    const
content = slide.querySelector('.banner-content');
if (content)
{
    content.classList.remove('text-enter');
content.onanimationend = null;
}
});
const
activeSlide = bannerSlides[bannerCarouselPosition];
if (!activeSlide) return;
const
content = activeSlide.querySelector('.banner-content');
if (!content) return;
void
content.offsetWidth;
content.classList.add('text-enter');
content.onanimationend = event = > {
    const
hasSubtitle = Boolean(content.querySelector('span'));
const
isLastAnimation = event.animationName == = 'banner-subtitle-enter'
                                           | | (!hasSubtitle & & event.animationName == = 'banner-title-enter');
if (!isLastAnimation)
return;
content.classList.remove('text-enter');
content.onanimationend = null;
};
}

function
settleInfiniteTransition()
{
if (!bannerTransitioning | | bannerPendingPosition == = null)
return;
clearTimeout(bannerTransitionTimer);
bannerTransitionTimer = null;
const
track = document.getElementById('bannerTrack');
if (track) track.ontransitionend = null;
const
count = bannerData.length;
bannerIndex = bannerPendingTargetIndex;
bannerCarouselPosition = bannerPendingPosition;
setInfiniteTrackPosition(bannerCarouselPosition, false);
if (bannerCarouselPosition === 0) {
bannerCarouselPosition = count;
setInfiniteTrackPosition(bannerCarouselPosition, false);
} else if (bannerCarouselPosition == = count + 1) {
bannerCarouselPosition = 1;
setInfiniteTrackPosition(bannerCarouselPosition, false);
}
markInfiniteActive();
bannerTransitioning = false;
bannerPendingTargetIndex = null;
bannerPendingPosition = null;
}

function
finishInfiniteTransition(targetIndex, requestedPosition)
{
clearTimeout(bannerTransitionTimer);
bannerTransitionTimer = null;
const
track = document.getElementById('bannerTrack');
if (track) track.ontransitionend = null;
const
slider = document.querySelector('#bannerSection .banner-slider');
const
count = bannerData.length;
bannerIndex = targetIndex;
bannerCarouselPosition = requestedPosition;
if (requestedPosition === 0) {
bannerCarouselPosition = count;
setInfiniteTrackPosition(bannerCarouselPosition, false);
} else if (requestedPosition == = count + 1) {
bannerCarouselPosition = 1;
setInfiniteTrackPosition(bannerCarouselPosition, false);
}
markInfiniteActive();
if (slider) slider.classList.remove('is-sliding');
replayInfiniteTextAnimation();
updateBannerDots();
bannerTransitioning = false;
bannerPendingTargetIndex = null;
bannerPendingPosition = null;
}

function
updateInfiniteSlider(targetIndex, direction='next', initial=false)
{
const
count = bannerData.length;
if (!count) return;
if (!initial & & bannerTransitioning) settleInfiniteTransition();
if (initial | | count === 1) {
bannerIndex = targetIndex;
bannerCarouselPosition = count > 1 ? targetIndex + 1: 0;
setInfiniteTrackPosition(bannerCarouselPosition, false);
markInfiniteActive();
const
slider = document.querySelector('#bannerSection .banner-slider');
if (slider)
slider.classList.remove('is-sliding');
replayInfiniteTextAnimation();
updateBannerDots();
return;
}

let
requestedPosition = targetIndex + 1;
if (direction === 'next' & & bannerIndex == = count - 1 & & targetIndex == = 0)
{
requestedPosition = count + 1;
} else if (direction === 'prev' & & bannerIndex == = 0 & & targetIndex == = count - 1) {
requestedPosition = 0;
}

bannerTransitioning = true;
bannerPendingTargetIndex = targetIndex;
bannerPendingPosition = requestedPosition;
bannerIndex = targetIndex;
updateBannerDots();
const
slider = document.querySelector('#bannerSection .banner-slider');
bannerSlides.forEach(slide= > {
    const
content = slide.querySelector('.banner-content');
if (content)
{
    content.classList.remove('text-enter');
content.onanimationend = null;
}
});
if (slider) slider.classList.add('is-sliding');
setInfiniteTrackPosition(requestedPosition, true);

const track = document.getElementById('bannerTrack');
track.ontransitionend = event = > {
if (event.target !== track | | event.propertyName != = 'transform') return;
track.ontransitionend = null;
finishInfiniteTransition(targetIndex, requestedPosition);
};
clearTimeout(bannerTransitionTimer);
bannerTransitionTimer = setTimeout(() = > finishInfiniteTransition(targetIndex,
                                                                   requestedPosition), BANNER_TRANSITION_MS + 120);
}

function
updateSpotlightSlider(targetIndex, initial=false)
{
    const
count = bannerData.length;
if (!count)
return;
clearTimeout(bannerTransitionTimer);
bannerTransitionTimer = null;
bannerTransitioning = false;
bannerIndex = targetIndex;
clearBannerSlideClasses();
const
activeSlide = bannerSlides.find(slide= > Number(slide.dataset.bannerIndex) == = targetIndex);
if (activeSlide) activeSlide.classList.add('active');
if (count > 1) {
const prevIndex = (targetIndex - 1 + count) %count;
const nextIndex = (targetIndex + 1) %count;
const prevSlide = bannerSlides.find(slide = > Number(slide.dataset.bannerIndex) == = prevIndex);
const nextSlide = bannerSlides.find(slide = > Number(slide.dataset.bannerIndex) == = nextIndex);
if (prevSlide) prevSlide.classList.add('prev');
if (nextSlide & & nextSlide != = prevSlide) nextSlide.classList.add('next');
}
updateBannerDots();
if (!initial) {
bannerTransitioning = true;
clearTimeout(bannerTransitionTimer);
bannerTransitionTimer = setTimeout(() = > {
bannerTransitioning = false;
bannerTransitionTimer = null;
}, BANNER_TRANSITION_MS);
}
}

function
applyBannerAnimationStyle(style)
{
const
slider = document.querySelector('#bannerSection .banner-slider');
const
section = document.getElementById('bannerSection');
const
track = document.getElementById('bannerTrack');
slider.classList.remove('banner-style-1', 'banner-style-2', 'banner-style-3');
slider.classList.remove('is-sliding');
slider.classList.add(`banner - style -${style}
`);
slider.classList.toggle('is-single', bannerData.length == = 1);
section.classList.toggle('banner-layout-expanded', style == = '2' | | style == = '3');
section.classList.toggle('banner-layout-style-2', style == = '2');
track.ontransitionend = null;
track.style.transition = 'none';
track.style.transform = '';
clearBannerSlideClasses();
if (style === '2') {
updateInfiniteSlider(0, 'next', true);
} else if (style == = '3') {
updateSpotlightSlider(0, true);
} else {
updateFadeSlider(0, true);
}
updateBannerArrows();
}

function
setActiveBanner(index, direction='next')
{
const
count = bannerData.length;
if (!count) return false;
const
targetIndex = (index + count) % count;
if (targetIndex === bannerIndex) return false;
if (bannerSettings.animation_style === '2') {
updateInfiniteSlider(targetIndex, direction);
} else if (bannerSettings.animation_style == = '3') {
updateSpotlightSlider(targetIndex);
} else {
updateFadeSlider(targetIndex);
}
return true;
}

function
moveBanner(delta, resetTimer=true)
{
const
direction = delta < 0 ? 'prev': 'next';
const
moved = setActiveBanner(bannerIndex + delta, direction);
if (resetTimer & & moved) restartBannerTimer();
}

function
restartBannerTimer()
{
clearInterval(bannerTimer);
bannerTimer = null;
if (bannerData.length <= 1) return;
const
seconds = Math.max(2, Math.min(20, Number(bannerSettings.transition_seconds) | | 4));
bannerTimer = setInterval(() = > moveBanner(1, false), seconds * 1000);
}

function
bannerSlideHtml(banner, index, clone='')
{
const
subtitle = banner.subtitle ? ` < span >${escapeHtml(banner.subtitle)} < / span > `: '';
const
cloneAttr = clone ? ` data - clone = "${clone}"
`: '';
return ` < div


class ="banner-slide${banner.link_url ? ' has-link' : ''}" data-banner-index="${index}"${cloneAttr}


style = "--banner-image:url('${safeCssImageUrl(banner.image, 'assets/banner3.png')}');" >
< div


class ="banner-content" > < strong > ${escapeHtml(banner.title)} < / strong > ${subtitle} < / div >

< / div > `;
}

function
bindBannerControls()
{
bannerDots.forEach(dot= > {
    dot.onclick = () = > {
    const
targetIndex = Number(dot.dataset.slide);
const
direction = targetIndex < bannerIndex ? 'prev': 'next';
if (setActiveBanner(targetIndex, direction))
restartBannerTimer();
};
});
bannerSlides.forEach(slide= > {
    slide.onpointerdown = event = > {
    bannerPointerStartX = event.clientX;
bannerPointerStartY = event.clientY;
bannerPointerMoved = false;
bannerPointerActive = true;
};
slide.onpointermove = event = > {
if (!bannerPointerActive)
return;
if (Math.abs(event.clientX - bannerPointerStartX) > 8 | | Math.abs(event.clientY - bannerPointerStartY) > 8) {
bannerPointerMoved = true;
}
};
slide.onpointerup = () = > {
bannerPointerActive = false;
};
slide.onpointercancel = () = > {
bannerPointerActive = false;
bannerPointerMoved = true;
};
slide.onclick = async () = > {
if (bannerTransitioning | | bannerPointerMoved) {
bannerPointerMoved = false;
return;
}
const
index = Number(slide.dataset.bannerIndex | | 0);
if (index !== bannerIndex)
return;
const
banner = bannerData[index] | | {};
const
url = String(banner.link_url | | '').trim();
if (!url) return;
if (Number(banner.id | | 0) > 0) {
apiPost('api/banner_click.php', {banner_id: Number(banner.id)}).catch(() = > {});
}
if (window.Telegram & & window.Telegram.WebApp & & typeof window.Telegram.WebApp.openLink == = 'function') {
window.Telegram.WebApp.openLink(url);
} else {
window.open(url, '_blank');
}
};
});
}

function
renderBanners(banners, settings={})
{
    const
list = Array.isArray(banners) ? banners: [];
const
section = document.getElementById('bannerSection');
const
track = document.getElementById('bannerTrack');
const
dots = document.getElementById('bannerDots');
stopBannerRuntime();
bannerData = list;
if (!list.length)
{
    section.classList.add('none');
updateBannerArrows();
return;
}

section.classList.remove('none');
bannerSettings = {
animation_style: ['1', '2', '3'].includes(String(settings.animation_style)) ? String(settings.animation_style): '1',
show_arrows: Number(settings.show_arrows == null ? 1: settings.show_arrows) == = 1 ? 1: 0,
transition_seconds: Math.max(2, Math.min(20, Number(settings.transition_seconds) | | 4))
};

const
realSlides = list.map((banner, index) = > bannerSlideHtml(banner, index)).join('');
if (bannerSettings.animation_style === '2' & & list.length > 1)
{
track.innerHTML = bannerSlideHtml(list[list.length - 1], list.length - 1, 'last')
+ realSlides
+ bannerSlideHtml(list[0], 0, 'first');
} else {
track.innerHTML = realSlides;
}
dots.innerHTML = list.length > 1
? list.map((_, index) = > ` < button


class ="banner-dot" data-slide="${index}" aria-label="${index + 1}-banner" > < / button > `).join('')
: '';
bannerSlides = [...track.querySelectorAll('.banner-slide')];
bannerDots = [...dots.querySelectorAll('.banner-dot')];
bannerIndex = 0;
bannerCarouselPosition = 0;
bindBannerControls();
applyBannerAnimationStyle(bannerSettings.animation_style);
restartBannerTimer();
}

async function
loadBanners()
{
try {
const res = await fetch('api/banners.php', {method: 'GET', cache: 'no-store'});
const
data = await res.json();
if (!res.ok | | !data.success | | !Array.isArray(data.banners)) throw
new
Error('banner_load_failed');
renderBanners(data.banners, data.settings | | {});
} catch(err)
{
    renderBanners([
        {id: 0, title: 'Chegirmalar', subtitle: "Eng mashhur o'yinlar uchun qulay narxlar", image: 'assets/banner3.png',
         link_url: ''},
        {id: 0, title: 'Tezkor xizmat', subtitle: 'Buyurtmalarni bir daqiqada topshirish', image: 'assets/banner2.png',
         link_url: ''},
        {id: 0, title: '24/7 Admin', subtitle: 'Har kuni doimiy faol xizmat', image: 'assets/banner02.png',
         link_url: ''}
    ], {animation_style: '1', show_arrows: 1, transition_seconds: 4});
}
}

function
bindCartSteppers()
{
document.querySelectorAll('.qty-plus').forEach(btn= > {
    btn.onclick = () = > {
    const
index = Number(btn.closest('[data-cart-index]').dataset.cartIndex);
cartItems[index].qty += 1;
clearAppliedPromo(false);
renderCart();
};
});
document.querySelectorAll('.qty-minus').forEach(btn= > {
    btn.onclick = () = > {
    const
index = Number(btn.closest('[data-cart-index]').dataset.cartIndex);
if (cartItems[index].qty > 1)
{
    cartItems[index].qty -= 1;
} else {
    cartItems.splice(index, 1);
}
clearAppliedPromo(false);
renderCart();
};
});
}

function
cartSubtotal()
{
return cartItems.reduce((sum, item) = > sum + item.price * item.qty, 0);
}

function
setPromoStatus(message, state='')
{
const
promoStatus = document.getElementById('promoStatus');
if (!promoStatus) return;
promoStatus.textContent = message;
promoStatus.classList.remove('success', 'error');
if (state) promoStatus.classList.add(state);
}

function
clearAppliedPromo(showMessage=true)
{
appliedPromo = null;
appliedDiscount = 0;
const
promoInput = document.getElementById('promoInput');
const
clearBtn = document.getElementById('clearPromoBtn');
if (clearBtn) clearBtn.classList.add('none');
if (promoInput) promoInput.disabled = false;
if (showMessage) setPromoStatus('Promo kod checkout buyurtmasiga qo‘llanadi.');
}

function
promoErrorText(error, fallback='')
{
const
map = {
    promo_not_found: 'Promo kod topilmadi',
    promo_inactive: 'Promo kod faol emas',
    promo_expired: 'Promo kod muddati tugagan',
    promo_not_started: 'Promo kod hali boshlanmagan',
    promo_usage_limit: 'Promo kod limiti tugagan',
    promo_already_used: 'Promo kod avval ishlatilgan',
    promo_new_users_only: 'Promo kod faqat yangi userlar uchun',
    promo_min_total_spent: 'Jami savdo yetarli emas',
    promo_min_order_amount: 'Buyurtma summasi yetarli emas',
    promo_invalid_amount: 'Summa noto‘g‘ri',
    request_timeout: 'Promo tekshiruvi sekinlashdi',
    network_error: 'Promo tekshirib bo‘lmadi'
};
return fallback | | map[error] | | 'Promo kod ishlamadi';
}

function
updateCheckoutSummary()
{
const
totalQty = cartItems.reduce((sum, item) = > sum + item.qty, 0);
const
subtotal = cartSubtotal();
if (appliedPromo & & Math.abs(Number(appliedPromo.subtotal | | 0) - subtotal) > 0.01) {
clearAppliedPromo(false);
setPromoStatus('Savat o‘zgardi. Promo kodni qayta qo‘llang.', 'error');
}
const
discount = Math.min(appliedDiscount, subtotal);
const
grand = Math.max(0, subtotal - discount);
lastGrandTotal = grand;
const
paymentNames = {uzcard: 'Uzcard', humo: 'Humo', balance: 'Balans', click: 'Click'};
document.getElementById('checkoutItemsCount').textContent = totalQty + ' ta';
document.getElementById('checkoutSubtotal').textContent = formatPrice(subtotal);
document.getElementById('checkoutDiscount').textContent = discount > 0 ? '-' + formatPrice(discount): formatPrice(0);
document.getElementById('checkoutGrandTotal').textContent = formatPrice(grand);
document.getElementById('checkoutPaymentName').textContent = paymentNames[selectedPayment] | | 'Uzcard';
const
summaryPromo = document.getElementById('summaryPromo');
if (summaryPromo) summaryPromo.textContent = appliedPromo ? appliedPromo.code: '—';
}

function
renderCart()
{
if (!cartItems.length) {
cartList.innerHTML = '<div class="summary-box" style="text-align:center;color:var(--text-muted);"><div style="font-size:42px;margin-bottom:8px;">🛒</div>Savat hozircha bo‘sh.</div>';
clearAppliedPromo(false);
summaryCount.textContent = '0 ta';
summaryTotal.textContent = '0 UZS';
updateCheckoutSummary();
return;
}

cartList.innerHTML = cartItems.map((item, i) = > `
< article


class ="cart-card" data-cart-index="${i}" >

< div


class ="cart-thumb" > < img src="${item.icon}" alt="icon" / > < / div >

< div


class ="cart-content" >

< div


class ="cart-title" > ${item.title} < / div >

< div


class ="cart-sub" > ${item.subtitle} < / div >

< div


class ="stepper" >

< button


class ="qty-minus" > − < / button >

< span


class ="qty-value" > ${item.qty} < / span >

< button


class ="qty-plus" > + < / button >

< / div >
< / div >
< div


class ="price" > ${formatPrice(item.price).replace(' UZS', '')} < small > UZS < / small > < / div >

< / article >
`).join('');

const
totalQty = cartItems.reduce((sum, item) = > sum + item.qty, 0);
const
totalPrice = cartItems.reduce((sum, item) = > sum + item.price * item.qty, 0);
summaryCount.textContent = totalQty + ' ta';
summaryTotal.textContent = formatPrice(totalPrice);
updateCheckoutSummary();
bindCartSteppers();
}

function
setSelectedGame(gameKey)
{
    activeGame = gameKey;
gameCards.forEach(card= > card.classList.toggle('is-selected', card.dataset.game == = gameKey));
}

function
bindProductCards()
{
    productCards.forEach(card= > {
        card.onclick = () = > openDetail(card.dataset.openDetail);
});
}

function
gameNeedle(gameKey)
{
    const
game = games[gameKey] | | {};
return `${gameKey | | ''} ${game.title | | ''} ${game.category | | ''}
`.toLowerCase();
}

function
isPremiumProduct(gameKey)
{
const
needle = gameNeedle(gameKey);
return needle.includes('telegram-premium') | | needle.includes('telegram premium') | | gameKey === 'premium';
}

function
isStarsProduct(gameKey)
{
const
needle = gameNeedle(gameKey);
return needle.includes('telegram-stars') | | needle.includes('telegram stars') | | gameKey === 'stars';
}

function
isUsernameProduct(gameKey)
{
return isPremiumProduct(gameKey) | | isStarsProduct(gameKey);
}

function
starUnitPrice(gameKey)
{
const
game = games[gameKey] | | {};
const
value = Number(game.star_unit_price | | 200);
return Number.isFinite(value) & & value >= 1 ? value: 200;
}

function
starMinAmount(gameKey)
{
const
game = games[gameKey] | | {};
const
value = Number(game.star_min_amount | | 50);
return Number.isFinite(value) & & value >= 50 ? Math.floor(value): 50;
}

function
starMaxAmount(gameKey)
{
const
game = games[gameKey] | | {};
const
value = Number(game.star_max_amount | | 1000000);
return Number.isFinite(value) & & value >= starMinAmount(gameKey) ? Math.floor(value): 1000000;
}

function
currentStarsAmount()
{
const
raw = String(starsAmountInput.value | | '').trim();
if (raw === '') return null;
const
value = Number(raw);
return Number.isInteger(value) ? value: null;
}

function
selectedPackageStarsAmount(gameKey)
{
const
game = games[gameKey];
if (!game | | !game.packages | | selectedPackageIndex == = null | | !game.packages[selectedPackageIndex]) {
return null;
}
return parseStarsAmountFromPackage(game.packages[selectedPackageIndex]);
}

function
effectiveStarsAmount(gameKey)
{
const
inputAmount = currentStarsAmount();
if (inputAmount !== null) return inputAmount;
return selectedPackageStarsAmount(gameKey);
}

function
currentDetailAmount(gameKey, pack)
{
if (isStarsProduct(gameKey)) {
const starsAmount = effectiveStarsAmount(gameKey);
return starsAmount === null ? null: starsAmount * starUnitPrice(gameKey);
}
return pack ? Number(pack.price | | 0): 0;
}

function
parseStarsAmountFromPackage(pack)
{
if (!pack) return null;
const
values = [
    pack.stars_amount,
    pack.amount,
    pack.name,
    pack.package_name,
    pack.product_id
];
for (const value of values) {
if (value == null | | value === '')
    continue;
const
direct = Number(value);
if (Number.isInteger(direct) & & direct > 0) return direct;
const
match = String(value).match( / (\d+) /);
if (match) {
const parsed = Number(match[1]);
if (Number.isInteger(parsed) & & parsed > 0)
return parsed;
}
}
return null;
}

function
findStarsPackageIndexByAmount(gameKey, amount)
{
const
game = games[gameKey];
if (!game | | !game.packages | | amount == = null) return null;
for (let i = 0; i < game.packages.length; i += 1) {
if (parseStarsAmountFromPackage(game.packages[i]) === amount) {
return i;
}
}
return null;
}

function
defaultStarsPackageIndex(gameKey)
{
const
minIndex = findStarsPackageIndexByAmount(gameKey, starMinAmount(gameKey));
if (minIndex !== null) return minIndex;
const
fiftyIndex = findStarsPackageIndexByAmount(gameKey, 50);
return fiftyIndex !== null ? fiftyIndex: 0;
}

function
selectedPackageForOrder(gameKey)
{
const
game = games[gameKey];
if (!game | | !game.packages | | !game.packages.length) return null;
if (!isStarsProduct(gameKey)) {
return game.packages[selectedPackageIndex] | | game.packages[0];
}
return selectedPackageIndex !== null & & game.packages[selectedPackageIndex]
? game.packages[selectedPackageIndex]
: game.packages[0];
}

function
syncStarsPackageSelectionFromAmount()
{
if (!isStarsProduct(activeGame)) return;
const
amount = currentStarsAmount();
if (amount === null) {
document.querySelectorAll('.package-btn').forEach(btn = > {
btn.classList.toggle('active', selectedPackageIndex != = null & & Number(btn.dataset.packIndex) == = selectedPackageIndex);
});
return;
}
const
matchedIndex = findStarsPackageIndexByAmount(activeGame, amount);
selectedPackageIndex = matchedIndex;
document.querySelectorAll('.package-btn').forEach(btn= > {
    btn.classList.toggle('active', matchedIndex != = null & & Number(btn.dataset.packIndex) == = matchedIndex);
});
}

function
updateDetailPrice()
{
    const
game = games[activeGame];
const
pack = selectedPackageForOrder(activeGame);
if (!game | | !pack)
return;
const
amount = currentDetailAmount(activeGame, pack);
document.getElementById('detailPrice').textContent = amount == = null ? 'Miqdor kiriting': formatPrice(amount);
}

function
usernamePlain(value)
{
return String(value | | '').trim().replace( / @ + / g, '');
}

function
normalizedTelegramUsername(value)
{
const
plain = usernamePlain(value);
return plain ? '@' + plain: '';
}

function
usernameValidationError(value)
{
const
plain = usernamePlain(value);
if (plain.length < 4) return 'Username kamida 4 ta belgi bo‘lsin';
if (plain.length > 32) return 'Username 32 ta belgidan oshmasin';
if (! / ^[A-Za-z0-9_]+$ /.test(plain)) return 'Faqat harf, raqam va _ ishlatish mumkin';
return '';
}

function
usernameModeErrorText(value)
{
return usernameValidationError(value);
}

function
isDefaultTelegramLogo(url)
{
return String(url | | '').trim().toLowerCase() === 'https://telegram.org/img/t_logo_2x.png';
}

function
setUsernameLookup(content, className='')
{
if (!usernameLookup) return;
usernameLookup.className = 'username-lookup show' + (className ? ' ' + className: '');
usernameLookup.innerHTML = content;
}

function
clearUsernameLookup()
{
if (usernameLookup) {
usernameLookup.className = 'username-lookup';
usernameLookup.innerHTML = '';
}
}

function
updateAddToCartAvailability()
{
if (!addToCartBtn) return;
addToCartBtn.disabled = Number(currentAppSettings.maintenance_mode | | 0) == = 1 & & Number(
    currentAppSettings.is_admin | | 0) != = 1;
}

function
resetUsernameLookup(mode='none')
{
if (usernameLookupTimer) {
clearTimeout(usernameLookupTimer);
usernameLookupTimer = null;
}
usernameLookupState = {
    mode,
    status: 'idle',
username: '',
found: false
};
clearUsernameLookup();
updateAddToCartAvailability();
}

function
renderUsernamePreview(data)
{
const
photo = normalizeImagePath(data.image_url | | data.photo | | '', 'assets/package.png');
const
username = usernamePlain(data.username | | usernameLookupState.username);
const
name = data.title | | data.name | | '@' + username;
return `
< div


class ="username-preview" >

< img
src = "${escapeHtml(photo)}"
alt = "${escapeHtml(username)}"
onerror = "this.src='assets/package.png'" / >
< div >
< strong >${escapeHtml(name)} < / strong >
< span >


@

${escapeHtml(username)} < / span >
< / div >
< / div >
`;
}

function
applyUsernameLookupResult(mode, plain, data)
{
const
result = Object.assign({}, data | | {}, {username: usernamePlain((data & & data.username) | | plain)});
usernameLookupState = {
    mode,
    status: 'found',
username: usernamePlain(result.username | | plain),
found: true
};
setUsernameLookup(renderUsernamePreview(result));
updateAddToCartAvailability();
}

async function
lookupTelegramUsername(gameKey, value)
{
const
plain = usernamePlain(value);
const
mode = isPremiumProduct(gameKey) ? 'premium': (isStarsProduct(gameKey) ? 'stars': 'none');

if (!plain) {
resetUsernameLookup(mode);
return;
}
const
validationError = usernameValidationError(plain);
if (validationError)
{
usernameLookupState = {mode, status: 'invalid', username: plain, found: false};
setUsernameLookup(validationError, 'error');
updateAddToCartAvailability();
return;
}
if (lastCheckedUsername === plain & & lastLookupResult) {
applyUsernameLookupResult(mode, plain, lastLookupResult);
return;
}

usernameLookupState = {mode, status: 'loading', username: plain, found: false};
updateAddToCartAvailability();
setUsernameLookup('Tekshirilmoqda...');
try {
const data = await apiPost('api/getinfo.php', {user: plain}, 10000);
if (data.found === false | | isDefaultTelegramLogo(data.image_url)) {
usernameLookupState = {mode, status: 'not_found', username: plain, found: false};
setUsernameLookup('Foydalanuvchi topilmadi', 'error');
updateAddToCartAvailability();
return;
}
usernameLookupState = {
mode,
status: 'found',
username: usernamePlain(data.username | | plain),
found: true
};
data.username = usernameLookupState.username;
lastCheckedUsername = usernameLookupState.username;
lastLookupResult = data;
setUsernameLookup(renderUsernamePreview(data));
updateAddToCartAvailability();
} catch(err)
{
    usernameLookupState = {mode, status: 'error', username: plain, found: false};
setUsernameLookup((err & & err.status === 401) ? 'Telegram auth xato': 'Tekshirib bo‘lmadi', 'error');
updateAddToCartAvailability();
}
}

function
scheduleUsernameLookup()
{
    clearInputError(playerIdWrap);
if (!isUsernameProduct(activeGame)) return;
const
mode = isPremiumProduct(activeGame) ? 'premium': 'stars';
const
plain = usernamePlain(playerIdInput.value);
if (usernameLookupTimer) clearTimeout(usernameLookupTimer);
if (!plain) {
resetUsernameLookup(mode);
return;
}
if (lastCheckedUsername === plain & & lastLookupResult) {
applyUsernameLookupResult(mode, plain, lastLookupResult);
return;
}
const
validationError = usernameValidationError(plain);
if (validationError)
{
usernameLookupState = {mode, status: 'invalid', username: plain, found: false};
setUsernameLookup(validationError, 'error');
updateAddToCartAvailability();
return;
}
usernameLookupState = {mode, status: 'loading', username: plain, found: false};
setUsernameLookup('Tekshirilmoqda...');
updateAddToCartAvailability();
usernameLookupTimer = setTimeout(() = > lookupTelegramUsername(activeGame, playerIdInput.value), 500);
}

function
setInputError(wrap, input, errorEl, message)
{
if (errorEl & & message)
errorEl.textContent = message;
if (wrap)
wrap.classList.add('error');
if (input)
input.focus();
}

function
clearInputError(wrap)
{
if (wrap)
wrap.classList.remove('error');
}

function
clearOrderInputErrors()
{
    clearInputError(playerIdWrap);
clearInputError(serverIdCard);
clearInputError(starsAmountWrap);
}

function
configureDetailInputs(gameKey, pack, preserveValues=false)
{
    const
usernameMode = isUsernameProduct(gameKey);
const
starsMode = isStarsProduct(gameKey);
clearOrderInputErrors();
if (!preserveValues)
{
resetUsernameLookup(usernameMode ? (isPremiumProduct(gameKey) ? 'premium': 'stars'): 'none');
playerIdInput.value = '';
serverIdInput.value = '';
starsAmountInput.value = '';
}
playerIdInput.type = usernameMode ? 'text': 'number';
playerIdInput.inputMode = usernameMode ? 'text': 'numeric';
playerIdInput.placeholder = usernameMode ? 'username': "O'yinchi ID";
playerIdWrap.classList.toggle('username-mode', usernameMode);
if (usernameMode)
{
playerIdInput.setAttribute('autocapitalize', 'off');
playerIdInput.setAttribute('autocomplete', 'off');
} else {
playerIdInput.removeAttribute('autocapitalize');
playerIdInput.removeAttribute('autocomplete');
}
serverIdCard.style.display = (!usernameMode & & pack & & pack.server_required) ? '': 'none';
starsAmountWrap.style.display = starsMode ? '': 'none';
if (starsMode)
{
starsAmountInput.min = String(starMinAmount(gameKey));
starsAmountInput.max = String(starMaxAmount(gameKey));
starsAmountInput.maxLength = 10;
starsAmountInput.placeholder = 'Miqdor';
}
serverIdInput.type = 'number';
serverIdInput.inputMode = 'numeric';
}

function
validateDetailInputs(gameKey, pack)
{
    clearOrderInputErrors();
const
usernameMode = isUsernameProduct(gameKey);
const
starsMode = isStarsProduct(gameKey);
const
playerId = usernameMode ? normalizedTelegramUsername(playerIdInput.value): playerIdInput.value.trim();
const
serverId = serverIdInput.value.trim();
if (!playerId)
{
setInputError(playerIdWrap, playerIdInput, playerIdError,
              usernameMode ? 'Username yozish kerak': "O'yinchi ID kiriting.");
return false;
}
const
usernameError = usernameMode ? usernameValidationError(playerId): '';
if (usernameMode & & usernameError)
{
setInputError(playerIdWrap, playerIdInput, playerIdError, usernameError);
return false;
}
if (usernameMode & & usernameLookupState.status === 'not_found') {
setInputError(playerIdWrap, playerIdInput, playerIdError, 'Foydalanuvchi topilmadi');
return false;
}
if (!usernameMode & & ! / ^ \d+$ /.test(playerId)) {
setInputError(playerIdWrap, playerIdInput, playerIdError, "O'yinchi ID faqat raqam bo‘lsin.");
return false;
}
if (!usernameMode & & pack.server_required) {
if (!serverId) {
setInputError(serverIdCard, serverIdInput, serverIdError, 'Server ID kiriting.');
return false;
}
if (! / ^ \d+$ /.test(serverId)) {
setInputError(serverIdCard, serverIdInput, serverIdError, 'Server ID faqat raqam bo‘lsin.');
return false;
}
}
if (starsMode) {
const starsAmount = effectiveStarsAmount(gameKey);
const minStars = starMinAmount(gameKey);
const maxStars = starMaxAmount(gameKey);
if (starsAmount == = null) {
setInputError(starsAmountWrap, starsAmountInput, starsAmountError, 'Miqdor yozish kerak');
return false;
}
if (!Number.isInteger(starsAmount) | | starsAmount < minStars) {
setInputError(starsAmountWrap, starsAmountInput, starsAmountError, minStars + ' dan kam bo‘lmasin');
return false;
}
if (starsAmount > maxStars) {
setInputError(starsAmountWrap, starsAmountInput, starsAmountError, maxStars + ' dan ko‘p bo‘lmasin');
return false;
}
}
return true;
}

function
validateStarsAmountLive()
{
if (!isStarsProduct(activeGame)) {
return true;
}
clearInputError(starsAmountWrap);
syncStarsPackageSelectionFromAmount();
const
starsAmount = effectiveStarsAmount(activeGame);
if (starsAmount === null)
{
updateDetailPrice();
return true;
}
const
minStars = starMinAmount(activeGame);
const
maxStars = starMaxAmount(activeGame);
if (!Number.isInteger(starsAmount) | | starsAmount < minStars) {
setInputError(starsAmountWrap, null, starsAmountError, minStars + ' dan kam bo‘lmasin');
updateDetailPrice();
return false;
}
if (starsAmount > maxStars) {
setInputError(starsAmountWrap, null, starsAmountError, maxStars + ' dan ko‘p bo‘lmasin');
updateDetailPrice();
return false;
}
updateDetailPrice();
return true;
}

function
openDetail(gameKey)
{
activeGame = gameKey;
const
game = games[gameKey];
if (!game) {
showToast('Mahsulot topilmadi.');
return;
}
selectedPackageIndex = isStarsProduct(gameKey) ? defaultStarsPackageIndex(gameKey): 0;
document.getElementById('detailTitle').textContent = game.title;
document.getElementById('detailSubtitle').textContent = game.subtitle;
document.getElementById('detailIconImg').src = normalizeImagePath(game.icon, 'assets/package.png');
document.getElementById('detailIconImg').alt = game.title;
document.getElementById('infoDelivery').textContent = game.delivery;
document.getElementById('infoType').textContent = game.type;
configureDetailInputs(gameKey, game.packages[0]);

packageList.innerHTML = game.packages.map((pack, index) = > {
    console.log('package_image', pack.image);
const
packageImage = normalizeImagePath(pack.image | | getPackageImage(gameKey, pack.name), 'assets/package.png');
const
priceText = isStarsProduct(gameKey) ? ('1 stars = ' + formatPrice(starUnitPrice(gameKey))): formatPrice(pack.price);
return `
< button


class ="package-btn ${index === selectedPackageIndex ? 'active' : ''}" data-pack-index="${index}" >

< div


class ="package-top" >

< img
src = "${escapeHtml(packageImage)}"
alt = "${escapeHtml(pack.name)}"


class ="package-img" onerror="this.src='assets/package.png'" / >

< div


class ="package-text" >

< strong >${escapeHtml(pack.name)} < / strong >
< / div >
< / div >
< span >${priceText} < / span >
< span >${escapeHtml(pack.note)} < / span >
< / button >
`;
}).join('');

updateDetailPrice();

document.querySelectorAll('.package-btn').forEach(btn= > {
btn.onclick = () = > {
    const
nextIndex = Number(btn.dataset.packIndex);
if (isStarsProduct(gameKey))
{
    const
packageAmount = parseStarsAmountFromPackage(game.packages[nextIndex]);
configureDetailInputs(gameKey, game.packages[nextIndex], true);
if (packageAmount !== null)
{
    starsAmountInput.value = String(packageAmount);
selectedPackageIndex = nextIndex;
syncStarsPackageSelectionFromAmount();
validateStarsAmountLive();
} else {
    updateDetailPrice();
}
return;
}
selectedPackageIndex = nextIndex;
document.querySelectorAll('.package-btn').forEach(x= > x.classList.remove('active'));
btn.classList.add('active');
configureDetailInputs(gameKey, game.packages[selectedPackageIndex], true);
updateDetailPrice();
};
});

detailBackdrop.classList.add('show');
detailPanel.classList.add('show');
}

function
closeDetail()
{
    detailBackdrop.classList.remove('show');
detailPanel.classList.remove('show');
}

function
openCheckout()
{
if (isMaintenanceBlocked())
return;
if (!cartItems.length) {
showToast('Avval savatga mahsulot qo‘shing.');
return;
}
updateCheckoutSummary();
checkoutBackdrop.classList.add('show');
checkoutPanel.classList.add('show');
}

function
closeCheckout()
{
    checkoutBackdrop.classList.remove('show');
checkoutPanel.classList.remove('show');
}

function
showStatusModal(type)
{
    statusBackdrop.classList.add('show');
[loadingModal, successModal, cancelModal].forEach(m= > m.classList.remove('show'));
if (type === 'loading') loadingModal.classList.add('show');
if (type == = 'success') successModal.classList.add('show');
if (type == = 'cancel') cancelModal.classList.add('show');
}

function closeStatusModals() {
statusBackdrop.classList.remove('show');
[loadingModal, successModal, cancelModal].forEach(m = > m.classList.remove('show'));
}

navItems.forEach(item = > item.addEventListener('click', () = > openPage(item.dataset.target)));

document.getElementById('balanceChip').addEventListener('click', () = > {
openPage('balance');
// showToast('Balans bo‘limi ochildi.');
});

document.getElementById('bannerPrev').addEventListener('click', () = > {
moveBanner(-1);
});

document.getElementById('bannerNext').addEventListener('click', () = > {
moveBanner(1);
});

window.addEventListener('resize', () = > {
if (bannerSettings.animation_style !== '2' | | !bannerData.length) return;
if (bannerTransitioning) settleInfiniteTransition();
setInfiniteTrackPosition(bannerCarouselPosition, false);
const
slider = document.querySelector('#bannerSection .banner-slider');
if (slider) slider.classList.remove('is-sliding');
replayInfiniteTextAnimation();
});

document.getElementById('openSelectedGame').addEventListener('click', () = > openDetail(activeGame));
document.getElementById('closeDetail').addEventListener('click', closeDetail);
detailBackdrop.addEventListener('click', closeDetail);

[...document.querySelectorAll('[data-game]')].forEach(card= > card.addEventListener('click', () = > {
    setSelectedGame(card.dataset.game);
openDetail(card.dataset.game);
}));

bindProductCards();

categoryChips.forEach(chip= > {
chip.addEventListener('click', () = > {
    categoryChips.forEach(c= > c.classList.remove('active'));
chip.classList.add('active');
const
filter = chip.dataset.filter;
gameCards.forEach(card= > {
    const
visible = filter == = 'all' | | card.dataset.category.includes(filter);
card.style.display = visible ? '': 'none';
});
});
});

document.getElementById('addToCartBtn').addEventListener('click', () = > {
if (isMaintenanceBlocked()) return;
const
game = games[activeGame];
const
pack = selectedPackageForOrder(activeGame);
if (!pack) {
showToast('Paket topilmadi.');
return;
}
const
packageImage = normalizeImagePath(pack.image | | getPackageImage(activeGame, pack.name), 'assets/package.png');
const
serverId = serverIdInput.value.trim();
if (!validateDetailInputs(activeGame, pack)) {
return;
}
const
usernameMode = isUsernameProduct(activeGame);
const
starsMode = isStarsProduct(activeGame);
const
playerId = usernameMode ? normalizedTelegramUsername(playerIdInput.value): playerIdInput.value.trim();
const
starsAmount = starsMode ? effectiveStarsAmount(activeGame): 0;
const
itemPrice = currentDetailAmount(activeGame, pack);
cartItems.push({
    icon: packageImage,
    title: starsMode ? `${game.title} — ${starsAmount}
stars
`: `${game.title} — ${pack.name}
`,
subtitle: `${usernameMode ? 'Username': "O'yinchi ID"}: ${playerId}${serverId ? ' / Server: ' + serverId: ''}${
    starsMode ? ' / Stars: ' + starsAmount: ''}`,
price: itemPrice,
qty: 1,
product_id: pack.id,
player_id: playerId,
server_id: usernameMode ? '': serverId,
stars_amount: starsAmount,
server_required: !usernameMode & & !!pack.server_required,
request_id: makeRequestId()
});
clearAppliedPromo(false);
renderCart();
closeDetail();
showToast(`${pack.name}
savatga
qo
'shildi.`);
});

document.getElementById('openCheckoutBtn').addEventListener('click', openCheckout);
document.getElementById('openPromoHint').addEventListener('click', openCheckout);
document.getElementById('closeCheckoutBtn').addEventListener('click', () = > showStatusModal('cancel'));
checkoutBackdrop.addEventListener('click', closeCheckout);

paymentCards.forEach(card= > {
card.addEventListener('click', () = > {
    paymentCards.forEach(x= > x.classList.remove('active'));
card.classList.add('active');
selectedPayment = card.dataset.payment;
updateCheckoutSummary();
});
});

balanceMethodCards.forEach(card= > {
card.addEventListener('click', () = > {
    balanceMethodCards.forEach(x= > x.classList.remove('active'));
card.classList.add('active');
const
methodText = document.getElementById('topupMethodText');
if (methodText)
methodText.textContent = card.querySelector('strong').textContent;
});
});

topupChips.forEach(chip= > {
chip.addEventListener('click', () = > {
    topupChips.forEach(x= > x.classList.remove('active'));
chip.classList.add('active');
clearInputError(customTopupWrap);
selectedTopupAmount = Number(chip.dataset.amount);
customTopupInput.value = '';
document.getElementById('topupAmountText').textContent = formatPrice(selectedTopupAmount);
validateTopupAmount();
});
});

playerIdInput.addEventListener('input', () = > {
clearInputError(playerIdWrap);
if (isUsernameProduct(activeGame) & & playerIdInput.value.indexOf('@') !== -1) {
playerIdInput.value = usernamePlain(playerIdInput.value);
}
scheduleUsernameLookup();
});
usernameSelfBtn.addEventListener('click', () = > {
if (!isUsernameProduct(activeGame)) return;
const
ownUsername = usernamePlain(user.username | | '');
if (!ownUsername) {
showToast('Usernameingiz yo‘q');
setInputError(playerIdWrap, playerIdInput, playerIdError, 'Usernameingiz yo‘q');
return;
}
clearInputError(playerIdWrap);
playerIdInput.value = ownUsername;
scheduleUsernameLookup();
});
serverIdInput.addEventListener('input', () = > clearInputError(serverIdCard));
starsAmountInput.addEventListener('input', () = > {
    const
digits = String(starsAmountInput.value | | '').replace( /\D + / g, '').slice(0, 10);
if (starsAmountInput.value !== digits)
{
starsAmountInput.value = digits;
}
validateStarsAmountLive();
});
customTopupInput.addEventListener('input', () = > {
    clearInputError(customTopupWrap);
const
maxDigits = String(Math.trunc(Number(currentAppSettings.max_topup | | 100000000))).length;
const
digits = String(customTopupInput.value | | '').replace( /\D / g, '').slice(0, maxDigits);
if (customTopupInput.value !== digits)
{
customTopupInput.value = digits;
}
const
val = Number(digits);
if (val > 0)
{
selectedTopupAmount = val;
topupChips.forEach(x= > x.classList.remove('active'));
document.getElementById('topupAmountText').textContent = formatPrice(selectedTopupAmount);
validateTopupAmount();
} else {
selectedTopupAmount = 0;
document.getElementById('topupAmountText').textContent = 'Miqdor kiriting';
}
});

function
validateTopupAmount()
{
    clearInputError(customTopupWrap);
const
minTopup = Number(currentAppSettings.min_topup | | 10000);
const
maxTopup = Number(currentAppSettings.max_topup | | 100000000);
const
minText = 'Minimal summa ' + minTopup.toLocaleString('uz-UZ') + ' so‘m';
const
maxText = 'Maksimal summa ' + maxTopup.toLocaleString('uz-UZ') + ' so‘m';
const
customValue = customTopupInput.value.trim();
if (customValue !== '')
{
    const
amount = Number(customValue.replace( /\D / g, ''));
if (!Number.isFinite(amount) | | amount < minTopup) {
setInputError(customTopupWrap, customTopupInput, customTopupError, minText);
return false;
}
if (amount > maxTopup) {
setInputError(customTopupWrap, customTopupInput, customTopupError, maxText);
return false;
}
selectedTopupAmount = amount;
}
if (!Number.isFinite(selectedTopupAmount) | | selectedTopupAmount < minTopup) {
setInputError(customTopupWrap, customTopupInput, customTopupError, minText);
return false;
}
if (selectedTopupAmount > maxTopup) {
setInputError(customTopupWrap, customTopupInput, customTopupError, maxText);
return false;
}
return true;
}

// document.getElementById('balanceTopupBtn').addEventListener('click', () = > {
                                                                               // showToast(
    formatPrice(selectedTopupAmount) + ' uchun to‘ldirish oynasi keyingi bosqichda ulanadi.');
//});
const
paymentModal = document.getElementById('paymentModal');
const
paymentLoadingOverlay = document.getElementById('paymentLoadingOverlay');

function
showPaymentLoading()
{
if (paymentLoadingOverlay) paymentLoadingOverlay.classList.add('show');
}

function
hidePaymentLoading()
{
if (paymentLoadingOverlay) paymentLoadingOverlay.classList.remove('show');
}

function
clearPaymentTimer()
{
if (paymentTimer) {
clearInterval(paymentTimer);
paymentTimer = null;
}
}

function
clearPaymentStatusPolling()
{
if (paymentStatusTimer) {
clearInterval(paymentStatusTimer);
paymentStatusTimer = null;
}
if (paymentCloseTimer) {
clearTimeout(paymentCloseTimer);
paymentCloseTimer = null;
}
}

function
closePaymentModal()
{
clearPaymentTimer();
clearPaymentStatusPolling();
paymentReviewing = false;
document.getElementById('paymentAmount').textContent = '';
document.getElementById('paymentAmountSubtitle').textContent = 'Summani aynan yuboring';
paymentModal.classList.remove('show');
tg.BackButton.hide();
}

function
setPaymentStatusText(text, isDanger)
{
const
statusPill = document.getElementById('paymentStatusPill');
if (!statusPill) return;
statusPill.classList.toggle('expired', !!isDanger);
statusPill.textContent = text;
}

function
setPaymentReviewingState()
{
paymentReviewing = true;
const
paidBtn = document.getElementById('paidBtn');
setPaymentStatusText('Tekshirilmoqda', false);
if (paidBtn) {
paidBtn.classList.remove('expired');
paidBtn.disabled = true;
paidBtn.textContent = 'Tekshirilmoqda...';
}
}

function
setPaymentExpiredState(isExpired)
{
const
paidBtn = document.getElementById('paidBtn');
const
cancelBtn = document.getElementById('cancelPaymentBtn');
const
timerCard = document.getElementById('paymentTimerCard');
if (timerCard) timerCard.classList.toggle('expired', isExpired);
if (isExpired) {
setPaymentStatusText('Muddati tugagan', true);
if (paidBtn) {
paidBtn.classList.add('expired');
paidBtn.disabled = true;
paidBtn.textContent = 'Muddati tugadi';
}
if (cancelBtn) cancelBtn.disabled = true;
return;
}
if (paymentReviewing) {
setPaymentReviewingState();
return;
}
setPaymentStatusText('Kutilmoqda', false);
if (paidBtn)
{
paidBtn.classList.remove('expired');
paidBtn.disabled = false;
paidBtn.textContent = "To'lov qildim";
}
if (cancelBtn) cancelBtn.disabled = false;
}

async function cancelCurrentPayment() {
if (paymentCancelSubmitting)
return;
if (!currentPaymentId) {
console.error('payment_cancel_missing_id', {pendingPayment});
showToast("To'lov topilmadi.");
return;
}
if (!hasTelegramAuth) {
showToast('Telegram orqali oching.');
return;
}

paymentCancelSubmitting = true;
const
cancelBtn = document.getElementById('cancelPaymentBtn');
const
paidBtn = document.getElementById('paidBtn');
if (cancelBtn)
cancelBtn.disabled = true;
if (paidBtn)
paidBtn.disabled = true;

try {
const result = await apiPost('api/cancel_payment.php', {payment_id: currentPaymentId});
if (result.status !== 'cancel') {
showToast(result.status == = 'expired' ? "To'lov muddati tugagan": "To'lov allaqachon qayta ishlangan");
} else {
    showToast("To'lov bekor qilindi");
}
pendingPayment = null;
currentPaymentId = null;
closePaymentModal();
refreshHistoryIfProfile();
loadUser();
} catch(err)
{
    console.error('payment_cancel_error', {
        payment_id: currentPaymentId,
        message: err.message,
        status: err.status | | 0,
        data: err.data | | null
    });
showToast(err.message == = 'request_timeout' ? "Bekor qilish so'rovi sekinlashdi.": "To'lov bekor qilinmadi.");
if (paymentReviewing) {
setPaymentReviewingState();
} else if (paidBtn) {
paidBtn.disabled = false;
}
} finally {
paymentCancelSubmitting = false;
if (cancelBtn) cancelBtn.disabled = false;
}
}

async function
refreshPaymentStatusOnce()
{
if (!currentPaymentId | | !hasTelegramAuth) return;
try {
const data = await apiPost('api/payment_status.php', {payment_id: currentPaymentId}, 10000);
handlePaymentStatus(data);
} catch(err)
{
    console.error('payment_status_poll_error', {
        payment_id: currentPaymentId,
        message: err.message,
        status: err.status | | 0,
        data: err.data | | null
    });
}
}

function
startPaymentStatusPolling()
{
clearPaymentStatusPolling();
refreshPaymentStatusOnce();
const
seconds = Math.max(1, Number(currentAppSettings.payment_poll_seconds | | 3));
paymentStatusTimer = setInterval(refreshPaymentStatusOnce, seconds * 1000);
}

function
stopPaymentActions()
{
const
paidBtn = document.getElementById('paidBtn');
const
cancelBtn = document.getElementById('cancelPaymentBtn');
if (paidBtn) paidBtn.disabled = true;
if (cancelBtn) cancelBtn.disabled = true;
}

function
handlePaymentStatus(data)
{
if (!data | | Number(data.payment_id) !== Number(currentPaymentId)) return;
const
status = normalizeStatus(data.status);

if (status === 'pending') {
return;
}

if (paymentStatusTimer) {
clearInterval(paymentStatusTimer);
paymentStatusTimer = null;
}

if (status === 'success') {
clearPaymentTimer();
paymentReviewing = false;
setPaymentStatusText('To‘lov tasdiqlandi', false);
stopPaymentActions();
showToast('Balansingiz to‘ldirildi');
if (typeof data.user_balance != = 'undefined') {
setBalance(data.user_balance);
}
loadUser();
refreshHistoryIfProfile();
paymentCloseTimer = setTimeout(() = > {
    pendingPayment = null;
currentPaymentId = null;
closePaymentModal();
}, 1500);
return;
}

if (status === 'cancel') {
const
label = data.cancel_reason == = 'admin_cancel'
? 'Bekor qilindi'
: (data.cancel_reason === 'user_cancel' ? 'Siz bekor qildingiz': 'Bekor qilingan');
clearPaymentTimer();
paymentReviewing = false;
setPaymentStatusText(label, true);
stopPaymentActions();
showToast(label);
pendingPayment = null;
currentPaymentId = null;
closePaymentModal();
refreshHistoryIfProfile();
loadUser();
return;
}

if (status === 'expired') {
setPaymentExpiredState(true);
stopPaymentActions();
refreshHistoryIfProfile();
}
}

function
startPaymentTimer(expiresTs, serverTime, createdTs)
{
    clearPaymentTimer();
const
timerEl = document.getElementById('timer');
const
progressEl = document.getElementById('paymentProgressFill');
const
finalExpiresTs = Number(expiresTs | | 0);
const
finalServerTime = Number(serverTime | | 0);
if (!Number.isFinite(finalExpiresTs) | | finalExpiresTs <= 0 | | !Number.isFinite(
    finalServerTime) | | finalServerTime <= 0) {
console.error('payment_timer_invalid_payload', {expires_ts: expiresTs, server_time: serverTime});
timerEl.textContent = '00:00';
if (progressEl) progressEl.style.width = '0%';
setPaymentExpiredState(true);
return;
}
const
finalCreatedTs = Number(createdTs | | 0);
const
totalSeconds = Math.max(1, finalExpiresTs - (Number.isFinite(finalCreatedTs) & & finalCreatedTs > 0
                                             ? finalCreatedTs: finalServerTime));
const
clientNow = Math.floor(Date.now() / 1000);
const
offset = finalServerTime - clientNow;

const
tick = () = > {
const
nowTs = Math.floor(Date.now() / 1000);
const
syncedNow = nowTs + offset;
const
remaining = finalExpiresTs - syncedNow;
console.log({
    server_time: finalServerTime,
    expires_ts: finalExpiresTs,
    nowTs,
    remaining
});
if (remaining <= 0) {
timerEl.textContent = '00:00';
if (progressEl) progressEl.style.width = '0%';
setPaymentExpiredState(true);
return false;
}
const
minutes = Math.floor(remaining / 60);
const
seconds = remaining % 60;
timerEl.textContent = String(minutes).padStart(2, '0') + ':' + String(seconds).padStart(2, '0');
if (progressEl)
{
const
progress = Math.max(0, Math.min(100, (remaining / totalSeconds) * 100));
progressEl.style.width = progress + '%';
}
setPaymentExpiredState(false);
return true;
};

if (tick()) {
paymentTimer = setInterval(() = > {
if (!tick()) clearPaymentTimer();
}, 1000);
}
}

function
renderPaymentCards(cards, selectedCardId)
{
    const
track = document.querySelector('.card-track');
const
dotsWrap = document.getElementById('cardDots');
const
countEl = document.getElementById('paymentCardCount');
const
list = (cards & & cards.length) ? cards: [];
if (countEl)
countEl.textContent = list.length + ' ta';
track.innerHTML = list.map((card, index) = > `
< div


class ="payment-bank-card active" data-card-id="${Number(card.id)}" data-selected="${Number(card.id) === selectedCardId ? '1' : '0'}" >

< div


class ="payment-card-top" >

< span >${escapeHtml(card.title)} < / span >
< span


class ="card-badge" > ${index + 1} / ${list.length} < / span >

< / div >
< div


class ="payment-card-number" > ${escapeHtml(card.card_number)} < / div >

< button


class ="payment-card-copy copy-card-btn" type="button" data-card-number="${escapeHtml(card.card_number)}" aria-label="Karta raqamini nusxalash" >

< ion - icon
name = "copy-outline" > < / ion - icon >
< / button >
< div


class ="payment-card-owner" > ${escapeHtml(card.owner_name)} < / div >

< / div >
`).join('');
dotsWrap.innerHTML = list.map((_, index) = > ` < span


class ="dot${index === 0 ? ' active' : ''}" > < / span > `).join('');
track.scrollLeft = 0;

track.querySelectorAll('.copy-card-btn').forEach(btn = > {
btn.onclick = () = > {
navigator.clipboard.writeText(btn.dataset.cardNumber | | '');
showToast('Karta nusxalandi');
};
});

const updateDots = () = > {


const
slide = track.querySelector('.payment-bank-card');
const
dots = [...dotsWrap.querySelectorAll('.dot')];
if (!slide | | !dots.length) return;
const
gap = 14;
const
step = slide.offsetWidth + gap;
const
index = Math.max(0, Math.min(dots.length - 1, Math.round(track.scrollLeft / step)));
dots.forEach((dot, i) = > dot.classList.toggle('active', i == = index));
};
track.onscroll = updateDots;
updateDots();
}

function
openPaymentModal(paymentData)
{
if (!paymentData | | !paymentData.payment_id | | !paymentData.expires_ts | | !paymentData.server_time)
{
console.error('payment_modal_invalid_payload', paymentData);
showToast("To'lov ma'lumoti noto'g'ri.");
return;
}
pendingPayment = paymentData;
currentPaymentId = paymentData.payment_id;
currentPaymentAmount = Number(paymentData.pay_amount | | paymentData.amount | | 0);
paymentReviewing = false;
const
cards = (paymentData.cards & & paymentData.cards.length) ? paymentData.cards: (paymentData.card ?[paymentData.card]:[]);
selectedPaymentCardId = Number(
    paymentData.selected_card_id | | paymentData.card_id | | (paymentData.card & & paymentData.card.id) | | (
                cards[0] & & cards[0].id) | | 0);
renderPaymentCards(cards, selectedPaymentCardId);
document.getElementById('paymentAmount').textContent = formatPrice(currentPaymentAmount);
const
requestedAmount = Number(paymentData.requested_amount | | currentPaymentAmount);
document.getElementById(
    'paymentAmountSubtitle').textContent = requestedAmount & & requestedAmount != = currentPaymentAmount
? 'Aniqlash uchun summa avtomatik moslandi' \
    : 'Summani aynan yuboring';
startPaymentTimer(paymentData.expires_ts, paymentData.server_time, paymentData.created_ts);
startPaymentStatusPolling();
paymentModal.classList.add('show');
tg.BackButton.show();
}

document.getElementById('balanceTopupBtn').addEventListener('click', async () = > {
if (paymentSubmitting) {
return;
}
if (isMaintenanceBlocked()) {
return;
}
if (!validateTopupAmount()) {
return;
}
if (!hasTelegramAuth) {
showToast('Telegram orqali oching.');
return;
}
paymentSubmitting = true;
document.getElementById('balanceTopupBtn').disabled = true;
showPaymentLoading();
try {
const activePayment = await apiPost('api/active_payment.php');
if (activePayment.active) {
showToast("Avvalgi to‘lovingiz hali faol");
hidePaymentLoading();
openPaymentModal(activePayment);
return;
}

const
payment = await apiPost('api/create_payment.php', {
    amount: selectedTopupAmount,
    request_id: makeRequestId()
});
if (payment.reused)
{
showToast("Avvalgi to‘lovingiz hali faol");
}
hidePaymentLoading();
openPaymentModal(payment);
} catch(err)
{
    hidePaymentLoading();
console.error('payment_create_error', {
    message: err.message,
    status: err.status | | 0,
    data: err.data | | null
});
showToast(err.status == = 401 ? 'Telegram auth xato.': (err.data & & err.data.message
                                                        ? err.data.message: (err.message == = 'request_timeout' ? "To'lov so'rovi sekinlashdi.": "To'lov yaratilmadi.")));
} finally {
    paymentSubmitting = false;
hidePaymentLoading();
document.getElementById('balanceTopupBtn').disabled = false;
}
});
document.getElementById('copyAmount').onclick = () = > {
    navigator.clipboard.writeText(
        currentPaymentAmount | | (pendingPayment ? pendingPayment.amount: selectedTopupAmount));
showToast("Summa nusxalandi");
};
document.getElementById('closePayment').onclick = closePaymentModal;
document.getElementById('paidBtn').onclick = () = > {
if (document.getElementById('paidBtn').disabled)
return;
setPaymentReviewingState();
startPaymentStatusPolling();
showToast("Tekshirilmoqda");
};
document.getElementById('cancelPaymentBtn').onclick = cancelCurrentPayment;

document.getElementById('balanceCancelBtn').addEventListener('click', () = > openPage('profile'));
document.getElementById('goProfileBtn').addEventListener('click', () = > openPage('profile'));

function
enableSwipeToClose(panel, backdrop, closeFn)
{
let
startY = 0;
let
currentY = 0;
let
dragging = false;
let
started = false;

const
dragHandle = panel.querySelector('.grabber');
if (!dragHandle) return;

function
getY(e)
{
return e.touches ? e.touches[0].clientY: e.clientY;
}

function
setDragProgress(diff)
{
const
panelHeight = panel.offsetHeight | | 1;
const
progress = Math.max(0, Math.min(diff / panelHeight, 1));
const
backdropOpacity = 1 - progress;

panel.style.transform = `translateX(-50 %)
translateY(${diff}
px)`;
backdrop.style.opacity = backdropOpacity;
}

function
resetStyles()
{
panel.style.transform = '';
backdrop.style.opacity = '';
}

function
onStart(e)
{
startY = getY(e);
currentY = startY;
dragging = false;
started = true;
panel.classList.add('dragging');
}

function
onMove(e)
{
if (!started) return;

currentY = getY(e);
const
diff = currentY - startY;

if (diff > 0) {
dragging = true;
setDragProgress(diff);
}
}

function
onEnd()
{
if (!started) return;

const
diff = currentY - startY;
panel.classList.remove('dragging');

if (dragging & & diff > 120) {
resetStyles();
closeFn();
} else {
resetStyles();
}

startY = 0;
currentY = 0;
dragging = false;
started = false;
}

dragHandle.addEventListener('touchstart', onStart, {passive: true});
dragHandle.addEventListener('touchmove', onMove, {passive: true});
dragHandle.addEventListener('touchend', onEnd);

dragHandle.addEventListener('mousedown', onStart);
window.addEventListener('mousemove', onMove);
window.addEventListener('mouseup', onEnd);
}

function
getGameImage(title)
{
if (title.includes('Mobile Legends'))
return 'assets/mlbb.png';
if (title.includes('PUBG')) return 'assets/pubg.png';
if (title.includes('Free Fire')) return 'assets/freefire.png';
if (title.includes('Balans')) return 'assets/topup2.png';
if (title.includes('Telegram Stars')) return 'assets/stars.png';
if (title.includes('Telegram Premium')) return 'assets/premium.png';
return 'assets/default.jpg';
}


let
historyData = [];

let
activeTab = 'orders';
let
activeStatus = 'all';

function
shouldPollOrderHistory(page=currentPage)
{
return page === 'profile';
}

function
stopHistoryOrdersPolling()
{
if (historyOrdersTimer) {
clearInterval(historyOrdersTimer);
historyOrdersTimer = null;
}
}

function
startHistoryOrdersPolling(page=currentPage)
{
if (historyOrdersTimer | | !shouldPollOrderHistory(page)) return;
historyOrdersTimer = setInterval(() = > {
if (!shouldPollOrderHistory()) {
    stopHistoryOrdersPolling();
return;
}
loadHistory({silent: true});
}, Math.max(1, Number(currentAppSettings.history_poll_seconds | | 5)) * 1000);
}

function
updateHistoryOrdersPolling(page=currentPage)
{
if (shouldPollOrderHistory(page))
{
if (!historyLoaded)
{
    loadHistory();
}
startHistoryOrdersPolling(page);
} else {
    stopHistoryOrdersPolling();
}
}

function
refreshHistoryIfProfile(options={})
{
if (currentPage !== 'profile')
return;
loadHistory(options);
}

function
normalizeStatus(status)
{
status = String(status | | '').toLowerCase();
if (status === 'done') return 'done';
if (status === 'processing') return 'processing';
if (status === 'failed') return 'failed';
if (status === 'paid' | | status == = 'completed' | | status == = 'success') return 'success';
if (status === 'expired') return 'expired';
if (status === 'cancel' | | status == = 'cancelled' | | status == = 'canceled') return 'cancel';
return 'pending';
}

async function
loadHistory(options={})
{
const
silent = Boolean(options.silent);
if (!hasTelegramAuth) {
historyData =[];
renderHistory();
return;
}
try {
const data = await apiPost('api/history.php');
const orders = (data.orders | |[]).map(item = > ({
type: 'order',
title: Number(item.stars_amount | | 0) >= 50 ? `${item.title} — ${Number(item.stars_amount)}
stars
`: `${item.title} ${item.package_name}
`,
image: item.image | | '',
amount: Number(item.amount),
discount_amount: Number(item.discount_amount | | 0),
promo_code: item.promo_code | | '',
status: normalizeStatus(item.status),
stars_amount: Number(item.stars_amount | | 0),
time: (item.created_at | | '').slice(11, 16)
}));
const
payments = (data.payments | | []).map(item= > ({
    type: 'payment',
    title: 'Balans to‘ldirish',
    image: item.image | | 'assets/topup2.png',
    amount: Number(item.amount),
    status: normalizeStatus(item.status),
    cancel_reason: item.cancel_reason | | '',
    time: (item.created_at | | '').slice(11, 16)
}));
historyData = orders.concat(payments);
historyLoaded = true;
renderHistory();
} catch(err)
{
if (!silent)
{
    historyData = [];
renderHistory();
}
console.error('history_load_error', {
    message: err.message,
    status: err.status | | 0,
    data: err.data | | null
});
if (!silent)
{
    showToast(err.message == = 'request_timeout' ? 'Tarix yuklanishi sekinlashdi.': 'Tarix backenddan yuklanmadi.');
}
}
}

function
renderHistory()
{
const
list = document.getElementById('historyList');
list.innerHTML = '';

const
filtered = historyData.filter(item= > {
if (activeTab === 'orders' & & item.type != = 'order')
return false;
if (activeTab === 'payments' & & item.type != = 'payment') return false;
if (activeStatus === 'success' & & item.status == = 'done') return true;
if (activeStatus !== 'all' & & item.status != = activeStatus) return false;
return true;
});

filtered.forEach(item= > {
const
el = document.createElement('div');
el.className = 'history-item';

let
statusText = '';
let
statusClass = '';

if (item.status === 'success') {
statusText = item.cancel_reason == = 'business_auto'
? 'Avto tasdiqlandi'
: 'Muvaffaqiyatli';
statusClass = 'status-success';
}
if (item.status === 'done') {
statusText = 'Bajarildi';
statusClass = 'status-success';
}
if (item.status === 'pending') {
statusText = 'Kutilmoqda';
statusClass = 'status-pending';
}
if (item.status === 'processing') {
statusText = 'Jarayonda';
statusClass = 'status-processing';
}
if (item.status === 'failed') {
statusText = 'Xatolik';
statusClass = 'status-failed';
}
if (item.status === 'cancel') {
statusText = item.cancel_reason == = 'user_cancel'
? 'Siz bekor qildingiz'
: (item.cancel_reason === 'admin_cancel' ? 'Admin bekor qildi': 'Bekor qilingan');
statusClass = 'status-cancel';
}
if (item.status === 'expired') {
statusText = 'Muddati tugagan';
statusClass = 'status-expired';
}
const
discountLine = item.discount_amount > 0
? ` < div


class ="history-status status-success" > Chegirma: -

${formatPrice(item.discount_amount)} < / div > `
: '';

el.innerHTML = `
< div


class ="history-row" >

< div


class ="history-left" >

< img
src = "${escapeHtml(item.image || getGameImage(item.title))}"


class ="history-img" / >

< div >
< div


class ="history-title" > ${escapeHtml(item.title)} < / div >

< div


class ="history-price" > ${item.amount.toLocaleString()} UZS < / div >

${discountLine}
< / div >
< / div >

< div


class ="history-right" >

< div


class ="history-time" > ${item.time | | '12:45'} < / div >

< div


class ="history-status ${statusClass}" > ${statusText} < / div >

< / div >

< / div >
`;

list.appendChild(el);
});

if (!filtered.length) {
list.innerHTML = '<div class="history-item" style="text-align:center;color:var(--text-muted);">Hozircha tarix yo‘q.</div>';
}
}


document.querySelectorAll('[data-tab]').forEach(btn = > {
btn.onclick = () = > {
document.querySelectorAll('[data-tab]').forEach(b= > b.classList.remove('active'));
btn.classList.add('active');
activeTab = btn.dataset.tab;
renderHistory();
loadHistory({silent: true});
updateHistoryOrdersPolling();
};
});

document.querySelectorAll('.filter-chip').forEach(btn= > {
    btn.onclick = () = > {
document.querySelectorAll('.filter-chip').forEach(b= > b.classList.remove('active'));
btn.classList.add('active');
activeStatus = btn.dataset.status;
renderHistory();
};
});

renderHistory();

document.getElementById('discountsCard').addEventListener('click', openDiscountsModal);
document.getElementById('referralsCard').addEventListener('click', openReferralsModal);
document.getElementById('closeReferralsModal').addEventListener('click', closeReferralsModal);
document.getElementById('copyReferralLink').addEventListener('click', copyReferralLink);
document.getElementById('shareReferralLink').addEventListener('click', shareReferralLink);
referralsBackdrop.addEventListener('click', closeReferralsModal);
document.getElementById('adminSupportCard').addEventListener('click', openAdminSupport);
document.getElementById('closeDiscountsModal').addEventListener('click', closeDiscountsModal);
discountsBackdrop.addEventListener('click', closeDiscountsModal);
document.querySelectorAll('[data-promo-tab]').forEach(btn= > {
    btn.onclick = () = > {
activePromoTab = btn.dataset.promoTab;
document.querySelectorAll('[data-promo-tab]').forEach(tab= > tab.classList.toggle('active', tab == = btn));
renderDiscountsList();
};
});




document.getElementById('applyPromoBtn').addEventListener('click', async () = > {
    const
code = document.getElementById('promoInput').value.trim().toUpperCase();
const
subtotal = cartSubtotal();
const
applyBtn = document.getElementById('applyPromoBtn');
const
clearBtn = document.getElementById('clearPromoBtn');
if (!code)
{
clearAppliedPromo(false);
setPromoStatus('Kod kiritilmadi.', 'error');
return;
}
if (!cartItems.length | | subtotal <= 0) {
clearAppliedPromo(false);
setPromoStatus('Avval savatga mahsulot qo‘shing.', 'error');
return;
}
if (!hasTelegramAuth) {
setPromoStatus('Telegram orqali oching.', 'error');
return;
}
applyBtn.disabled = true;
setPromoStatus('Promo tekshirilmoqda...');
try {
const data = await apiPost('api/apply_promocode.php', {code, amount: subtotal}, 10000);
appliedPromo = {
    code: data.code | | code,
    discount: Number(data.discount_amount | | 0),
    final: Number(data.final_amount | | subtotal),
    subtotal
};
appliedDiscount = appliedPromo.discount;
document.getElementById('promoInput').value = appliedPromo.code;
document.getElementById('promoInput').disabled = true;
if (clearBtn)
clearBtn.classList.remove('none');
setPromoStatus('Promo kod qo‘llandi: -' + formatPrice(appliedDiscount), 'success');
} catch(err)
{
    clearAppliedPromo(false);
const
message = promoErrorText(err.message, err.data & & err.data.message ? err.data.message: '');
setPromoStatus(message, 'error');
showToast(message);
} finally {
    applyBtn.disabled = false;
updateCheckoutSummary();
}
});

document.getElementById('clearPromoBtn').addEventListener('click', () = > {
const
promoInput = document.getElementById('promoInput');
clearAppliedPromo(true);
if (promoInput) promoInput.value = '';
updateCheckoutSummary();
});

document.getElementById('confirmCheckoutBtn').addEventListener('click', async () = > {
if (orderSubmitting) {
return;
}
if (isMaintenanceBlocked()) {
return;
}
if (!cartItems.length) {
showToast('Savat bo‘sh.');
return;
}
if (!hasTelegramAuth) {
showToast('Telegram orqali oching.');
return;
}
if (cartItems.some(item= > !item.product_id)) {
showToast('Mahsulotlar backenddan yuklanmadi.');
return;
}
orderSubmitting = true;
closeCheckout();
showStatusModal('loading');
try {
let lastOrder = null;
let actualGrandTotal = 0;
let promoSent = false;
for (const item of cartItems) {
for (let i = 0; i < item.qty; i += 1) {
const promoCodeForOrder = (!promoSent & & appliedPromo) ? appliedPromo.code: '';
lastOrder = await apiPost('api/create_order.php', {
    product_id: item.product_id,
    player_id: item.player_id,
    server_id: item.server_id | | '',
    stars_amount: item.stars_amount | | 0,
    promo_code: promoCodeForOrder,
    request_id: item.request_id + '-' + i
});
if
(promoCodeForOrder)
promoSent = true;
actualGrandTotal += Number(lastOrder.amount | | 0);
}
}
lastGrandTotal = actualGrandTotal;
closeStatusModals();
const
orderPrefix = lastOrder & & lastOrder.order_prefix ? String(lastOrder.order_prefix): 'GS';
document.getElementById('successOrderId').textContent = '#' + orderPrefix + '-' + (lastOrder ? lastOrder.order_id: '');
document.getElementById('successAmount').textContent = formatPrice(lastGrandTotal);
if (lastOrder & & (lastOrder.public_send_ok === false | | lastOrder.admin_send_ok == = false))
{
    console.error('order_channel_send_failed', {
        public_send_ok: lastOrder.public_send_ok,
        admin_send_ok: lastOrder.admin_send_ok,
        public_error: lastOrder.public_error | | '',
        admin_error: lastOrder.admin_error | | ''
    });
}
cartItems.length = 0;
clearAppliedPromo(false);
renderCart();
loadUser();
refreshHistoryIfProfile();
showStatusModal('success');
} catch(err)
{
    closeStatusModals();
console.error('order_create_error', {
    message: err.message,
    status: err.status | | 0,
    data: err.data | | null
});
if (err.status === 402)
{
    showToast('Balans yetarli emas.');
openPage('balance');
} else if (err.data & & err.data.error === 'server_id_required') {
showToast('Server ID majburiy.');
} else if (err.message & & err.message.indexOf('promo_') == = 0) {
showToast(promoErrorText(err.message, err.data & & err.data.message ? err.data.message: ''));
} else if (err.data & & err.data.error === 'stars_amount_required') {
showToast('Kamida 50 stars kiriting.');
} else if (err.data & & err.data.error == = 'stars_amount_too_large') {
showToast('Stars miqdori limitdan katta.');
} else if (err.data & & (err.data.error == = 'stars_price_not_configured' | | err.data.error == = 'stars_max_not_configured')) {
showToast('Stars sozlamalari to‘liq emas.');
} else if (err.data & & err.data.error == = 'username_invalid') {
showToast('Username noto‘g‘ri.');
} else if (err.message == = 'request_timeout') {
showToast('Buyurtma so‘rovi sekinlashdi. Tarixni tekshiring.');
loadUser();
refreshHistoryIfProfile();
} else {
showToast('Buyurtma yaratilmadi.');
}
} finally {
orderSubmitting = false;
}
});

document.getElementById('closeSuccessBtn').addEventListener('click', closeStatusModals);
document.getElementById('successProfileBtn').addEventListener('click', () = > {
closeStatusModals();
openPage('profile');
showToast('Buyurtma ma’lumoti saqlandi.');
});

document.getElementById('cancelDismissBtn').addEventListener('click', closeStatusModals);
document.getElementById('cancelConfirmBtn').addEventListener('click', () = > {
closeStatusModals();
closeCheckout();
showToast('Checkout yopildi.');
});

statusBackdrop.addEventListener('click', closeStatusModals);

document.getElementById('clearCart').addEventListener('click', () = > {
cartItems.length = 0;
appliedDiscount = 0;
appliedPromo = null;
document.getElementById('promoInput').value = '';
document.getElementById('promoInput').disabled = false;
document.getElementById('clearPromoBtn').classList.add('none');
setPromoStatus('Promo kod checkout buyurtmasiga qo‘llanadi.');
renderCart();
closeCheckout();
showToast('Savat tozalandi.');
});

document.addEventListener('keydown', e= > {
if (e.key === 'Escape') {
closeDetail();
closeCheckout();
closeDiscountsModal();
closeReferralsModal();
closeStatusModals();
}
});

loadBanners();
renderCart();
updateHeaderForPage(currentPage);
loadUser();
loadProducts();

enableSwipeToClose(detailPanel, detailBackdrop, closeDetail);
enableSwipeToClose(checkoutPanel, checkoutBackdrop, closeCheckout);
< / script >
    < / body >

        < / html >
