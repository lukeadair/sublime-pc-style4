import sublime_plugin
import sublime


style4_classes = ["absolute-overlay","action-link","ajax-loader1","ajax-loader2","ajax-loader3","align-center","align-left","align-lg-down-center","align-lg-down-left","align-lg-down-right","align-lg-only-center","align-lg-only-left","align-lg-only-right","align-lg-up-center","align-lg-up-left","align-lg-up-right","align-md-down-center","align-md-down-left","align-md-down-right","align-md-only-center","align-md-only-left","align-md-only-right","align-md-up-center","align-md-up-left","align-md-up-right","align-right","align-sm-down-center","align-sm-down-left","align-sm-down-right","align-sm-only-center","align-sm-only-left","align-sm-only-right","align-sm-up-center","align-sm-up-left","align-sm-up-right","align-xs-down-center","align-xs-down-left","align-xs-down-right","align-xs-only-center","align-xs-only-left","align-xs-only-right","align-xs-up-center","align-xs-up-left","align-xs-up-right","aspect-16x9","aspect-1x1","aspect-2x1","aspect-2x3","aspect-3x1","aspect-3x2","aspect-3x4","aspect-4x1","aspect-4x3","aspect-5x1","aspect-5x2","aspect-6x1","aspect-7x1","aspect-8x1","bg-color-accent1-9","bg-color-accent1-C","bg-color-accent2-7","bg-color-accent2-9","bg-color-accent2-B","bg-color-accent2-C","bg-color-accent3-6","bg-color-accent3-D","bg-color-accent4-D","bg-color-accent5-8","bg-color-base-4","bg-color-base-A","bg-color-base-C","bg-color-base-D","bg-color-base-E","bg-color-black","bg-color-none","bg-color-white","bg-gradient-black-bottom","bg-gradient-black-left","bg-gradient-black-right","bg-gradient-black-top","bg-gradient-white-bottom","bg-gradient-white-left","bg-gradient-white-right","bg-gradient-white-top","big-p","bigtext1","block","blockquote-label","boldtext","border-box","border-color-accent1-9","border-color-accent1-C","border-color-accent2-7","border-color-accent2-9","border-color-accent2-B","border-color-accent2-C","border-color-accent3-6","border-color-accent3-D","border-color-accent4-D","border-color-accent5-8","border-color-base-4","border-color-base-A","border-color-base-C","border-color-base-D","border-color-base-E","border-color-black","border-color-none","border-color-white","borderless-form","btn-accent1","btn-accent1-outlined","btn-accent2","btn-accent2-outlined","btn-accent3","btn-accent3-outlined","btn-accent5","btn-accent5-outlined","btn-disabled","btn-disabled-outlined","btn-full","btn-large","btn-medium","btn-small","btn-white","btn-white-outlined","btn-wrap","btn-xsmall","btn3","by-text-input","center","center-child-vertically","center-v","center-v-h","centertext","check-radio-indent","check-radio-inline","cim-featurebox","cim-iframe-wrapper","clear","clearfix","clearfloat","clearfloats","clearleft","clearright","clickable","collapsed","color-accent1-9","color-accent1-C","color-accent2-7","color-accent2-9","color-accent2-B","color-accent2-C","color-accent3-6","color-accent3-D","color-accent4-D","color-accent5-8","color-base-4","color-base-A","color-base-C","color-base-D","color-base-E","color-black","color-none","color-white","containfloats","cri-secondary","CSS","disable-kern-lg","disable-kern-md","disable-kern-sm","disable-kern-xs","div-blocker","div-blocker-icon","div-blocker-parent","eliminate-descender-space","end","end-center","es-checkbox","es-collapsed-note","es-content","es-control","es-expanded-note","es-icon","es-no-border","es-no-collapsed-border","es-no-control-notes","es-title","expandable-section","expanded","ext-nav","ext-nav-plus","ext-open","field-error","fill-parent","first","floatleft","floatright","fluid-width-video-wrapper","font-gotham-rounded-bold","font-gotham-rounded-bold-italic","font-gotham-rounded-book","font-gotham-rounded-book-italic","font-gotham-rounded-medium","font-gotham-rounded-medium-italic","font-knockout-47","font-knockout-48","font-knockout-50","font-knockout-93","font-knockout-full-heavy","font-knockout-full-light","font-size-0-0em","font-size-0-1em","font-size-0-2em","font-size-0-3em","font-size-0-4em","font-size-0-5em","font-size-0-6em","font-size-0-7em","font-size-0-8em","font-size-0-9em","font-size-1-0em","font-size-1-1em","font-size-1-2em","font-size-1-3em","font-size-1-4em","font-size-1-5em","font-size-1-6em","font-size-1-7em","font-size-1-8em","font-size-1-9em","font-size-2-0em","font-size-2-1em","font-size-2-2em","font-size-2-3em","font-size-2-4em","font-size-2-5em","font-size-2-6em","font-size-2-7em","font-size-2-8em","font-size-2-9em","font-size-3-0em","font-size-3-5em","font-size-4-0em","font-size-4-5em","font-size-5-0em","font-size-5-5em","galign-bottom","galign-center","galign-lg-bottom","galign-lg-center","galign-lg-stretch","galign-lg-top","galign-md-bottom","galign-md-center","galign-md-stretch","galign-md-top","galign-sm-bottom","galign-sm-center","galign-sm-stretch","galign-sm-top","galign-stretch","galign-top","galign-xs-bottom","galign-xs-center","galign-xs-stretch","galign-xs-top","gclear","gclear-lg-down","gclear-lg-only","gclear-lg-up","gclear-md-down","gclear-md-only","gclear-md-up","gclear-sm-down","gclear-sm-only","gclear-sm-up","gclear-xs-down","gclear-xs-only","gclear-xs-up","gcol-1","gcol-1-1","gcol-1-12","gcol-1-2","gcol-1-3","gcol-1-4","gcol-1-5","gcol-1-6","gcol-10-12","gcol-11-12","gcol-12-12","gcol-2-12","gcol-2-2","gcol-2-3","gcol-2-4","gcol-2-5","gcol-2-6","gcol-3-12","gcol-3-3","gcol-3-4","gcol-3-5","gcol-3-6","gcol-4-12","gcol-4-4","gcol-4-5","gcol-4-6","gcol-5-12","gcol-5-5","gcol-5-6","gcol-6-12","gcol-6-6","gcol-7-12","gcol-8-12","gcol-9-12","gcol-lg-1","gcol-lg-1-1","gcol-lg-1-12","gcol-lg-1-2","gcol-lg-1-3","gcol-lg-1-4","gcol-lg-1-5","gcol-lg-1-6","gcol-lg-10-12","gcol-lg-11-12","gcol-lg-12-12","gcol-lg-2-12","gcol-lg-2-2","gcol-lg-2-3","gcol-lg-2-4","gcol-lg-2-5","gcol-lg-2-6","gcol-lg-3-12","gcol-lg-3-3","gcol-lg-3-4","gcol-lg-3-5","gcol-lg-3-6","gcol-lg-4-12","gcol-lg-4-4","gcol-lg-4-5","gcol-lg-4-6","gcol-lg-5-12","gcol-lg-5-5","gcol-lg-5-6","gcol-lg-6-12","gcol-lg-6-6","gcol-lg-7-12","gcol-lg-8-12","gcol-lg-9-12","gcol-md-1","gcol-md-1-1","gcol-md-1-12","gcol-md-1-2","gcol-md-1-3","gcol-md-1-4","gcol-md-1-5","gcol-md-1-6","gcol-md-10-12","gcol-md-11-12","gcol-md-12-12","gcol-md-2-12","gcol-md-2-2","gcol-md-2-3","gcol-md-2-4","gcol-md-2-5","gcol-md-2-6","gcol-md-3-12","gcol-md-3-3","gcol-md-3-4","gcol-md-3-5","gcol-md-3-6","gcol-md-4-12","gcol-md-4-4","gcol-md-4-5","gcol-md-4-6","gcol-md-5-12","gcol-md-5-5","gcol-md-5-6","gcol-md-6-12","gcol-md-6-6","gcol-md-7-12","gcol-md-8-12","gcol-md-9-12","gcol-sm-1","gcol-sm-1-1","gcol-sm-1-12","gcol-sm-1-2","gcol-sm-1-3","gcol-sm-1-4","gcol-sm-1-5","gcol-sm-1-6","gcol-sm-10-12","gcol-sm-11-12","gcol-sm-12-12","gcol-sm-2-12","gcol-sm-2-2","gcol-sm-2-3","gcol-sm-2-4","gcol-sm-2-5","gcol-sm-2-6","gcol-sm-3-12","gcol-sm-3-3","gcol-sm-3-4","gcol-sm-3-5","gcol-sm-3-6","gcol-sm-4-12","gcol-sm-4-4","gcol-sm-4-5","gcol-sm-4-6","gcol-sm-5-12","gcol-sm-5-5","gcol-sm-5-6","gcol-sm-6-12","gcol-sm-6-6","gcol-sm-7-12","gcol-sm-8-12","gcol-sm-9-12","gcol-small-adjust-1","gcol-xs-1","gcol-xs-1-1","gcol-xs-1-12","gcol-xs-1-2","gcol-xs-1-3","gcol-xs-1-4","gcol-xs-1-5","gcol-xs-1-6","gcol-xs-10-12","gcol-xs-11-12","gcol-xs-12-12","gcol-xs-2-12","gcol-xs-2-2","gcol-xs-2-3","gcol-xs-2-4","gcol-xs-2-5","gcol-xs-2-6","gcol-xs-3-12","gcol-xs-3-3","gcol-xs-3-4","gcol-xs-3-5","gcol-xs-3-6","gcol-xs-4-12","gcol-xs-4-4","gcol-xs-4-5","gcol-xs-4-6","gcol-xs-5-12","gcol-xs-5-5","gcol-xs-5-6","gcol-xs-6-12","gcol-xs-6-6","gcol-xs-7-12","gcol-xs-8-12","gcol-xs-9-12","gif","gjustify-center","gjustify-left","gjustify-lg-center","gjustify-lg-left","gjustify-lg-right","gjustify-lg-space-around","gjustify-lg-space-between","gjustify-md-center","gjustify-md-left","gjustify-md-right","gjustify-md-space-around","gjustify-md-space-between","gjustify-right","gjustify-sm-center","gjustify-sm-left","gjustify-sm-right","gjustify-sm-space-around","gjustify-sm-space-between","gjustify-space-around","gjustify-space-between","gjustify-xs-center","gjustify-xs-left","gjustify-xs-right","gjustify-xs-space-around","gjustify-xs-space-between","gnowrap","gnowrap-lg","gnowrap-md","gnowrap-sm","gnowrap-xs","gpad-bottom-none","gpad-lg-loose","gpad-lg-none","gpad-lg-normal","gpad-lg-tight","gpad-lg-xloose","gpad-lg-xtight","gpad-lg-xxloose","gpad-lg-xxtight","gpad-loose","gpad-md-loose","gpad-md-none","gpad-md-normal","gpad-md-tight","gpad-md-xloose","gpad-md-xtight","gpad-md-xxloose","gpad-md-xxtight","gpad-none","gpad-normal","gpad-sm-loose","gpad-sm-none","gpad-sm-normal","gpad-sm-tight","gpad-sm-xloose","gpad-sm-xtight","gpad-sm-xxloose","gpad-sm-xxtight","gpad-tight","gpad-xloose","gpad-xs-loose","gpad-xs-none","gpad-xs-normal","gpad-xs-tight","gpad-xs-xloose","gpad-xs-xtight","gpad-xs-xxloose","gpad-xs-xxtight","gpad-xtight","gpad-xxloose","gpad-xxtight","graphic","greverse","greverse-lg","greverse-md","greverse-sm","greverse-xs","grid","gwidth-fluid","gwrap","gwrap-lg","gwrap-md","gwrap-sm","gwrap-xs","heading-condensed","heading-extended","heading-line","hidden-lg-down","hidden-lg-only","hidden-lg-up","hidden-md-down","hidden-md-only","hidden-md-up","hidden-sm-down","hidden-sm-only","hidden-sm-up","hidden-xs-down","hidden-xs-only","hidden-xs-up","hidetext","hover-bg-color-accent1-9","hover-bg-color-accent1-C","hover-bg-color-accent2-7","hover-bg-color-accent2-9","hover-bg-color-accent2-B","hover-bg-color-accent2-C","hover-bg-color-accent3-6","hover-bg-color-accent3-D","hover-bg-color-accent4-D","hover-bg-color-accent5-8","hover-bg-color-base-4","hover-bg-color-base-A","hover-bg-color-base-C","hover-bg-color-base-D","hover-bg-color-base-E","hover-bg-color-black","hover-bg-color-none","hover-bg-color-white","hover-border-color-accent1-9","hover-border-color-accent1-C","hover-border-color-accent2-7","hover-border-color-accent2-9","hover-border-color-accent2-B","hover-border-color-accent2-C","hover-border-color-accent3-6","hover-border-color-accent3-D","hover-border-color-accent4-D","hover-border-color-accent5-8","hover-border-color-base-4","hover-border-color-base-A","hover-border-color-base-C","hover-border-color-base-D","hover-border-color-base-E","hover-border-color-black","hover-border-color-none","hover-border-color-white","hover-color-accent1-9","hover-color-accent1-C","hover-color-accent2-7","hover-color-accent2-9","hover-color-accent2-B","hover-color-accent2-C","hover-color-accent3-6","hover-color-accent3-D","hover-color-accent4-D","hover-color-accent5-8","hover-color-base-4","hover-color-base-A","hover-color-base-C","hover-color-base-D","hover-color-base-E","hover-color-black","hover-color-none","hover-color-white","hover-underline","icn","icn-","icn-activities","icn-apple","icn-arrow-down","icn-arrow-left","icn-arrow-right","icn-arrow-stripes","icn-arrow-up","icn-arrows","icn-bank","icn-battery","icn-beachball","icn-book","icn-bunkbed","icn-calendar","icn-camera","icn-carabiner","icn-chain-link","icn-check","icn-checklist","icn-circle-arrow-down","icn-circle-arrow-down-thin","icn-circle-border","icn-circle-exclamation","icn-circle-fill","icn-circle-line-alarm","icn-circle-line-backpack","icn-circle-line-basketball","icn-circle-line-book","icn-circle-line-brokenheart","icn-circle-line-bus","icn-circle-line-calendar","icn-circle-line-carabiner","icn-circle-line-city","icn-circle-line-clipboard","icn-circle-line-clock","icn-circle-line-conversation","icn-circle-line-exclamationpoint","icn-circle-line-family","icn-circle-line-forge","icn-circle-line-heart","icn-circle-line-hills","icn-circle-line-house","icn-circle-line-kids","icn-circle-line-location","icn-circle-line-lunch","icn-circle-line-megaphone","icn-circle-line-microphone","icn-circle-line-money","icn-circle-line-partypopper","icn-circle-line-phone","icn-circle-line-present","icn-circle-line-questionmark","icn-circle-line-share","icn-circle-line-shovel","icn-circle-line-snowflake","icn-circle-line-star","icn-circle-line-suitcase","icn-circle-line-sun","icn-circle-line-tree","icn-circle-line-waves","icn-circle-question","icn-clap-board","icn-clock","icn-club-guitar","icn-credit-card","icn-dice","icn-document","icn-dollar-bill","icn-dollar-sign","icn-donut","icn-double-bar","icn-empty-box","icn-evening-program","icn-exclamation","icn-eye","icn-facebook-f","icn-facebook-round","icn-family","icn-fat-arrow-down","icn-fat-arrow-up","icn-flag","icn-flapjacks","icn-glasses","icn-hamburger","icn-hang-time","icn-heart-coin","icn-heart-house","icn-hot-dog","icn-house","icn-house-tree","icn-ice-cream-bar","icn-instagram","icn-iphone","icn-jeep","icn-key","icn-letter","icn-life-jacket","icn-lifejacket","icn-line-arrow-left","icn-line-arrow-right","icn-line-backpack","icn-line-basketball-goal","icn-line-book","icn-line-broken-heart","icn-line-bus","icn-line-calendar","icn-line-city","icn-line-clipboard","icn-line-conversation","icn-line-exclamation","icn-line-family","icn-line-fedora","icn-line-forge","icn-line-heart","icn-line-hills","icn-line-house","icn-line-lunch","icn-line-megaphone","icn-line-microphone","icn-line-money","icn-line-party-popper","icn-line-present","icn-line-shoe","icn-line-shovel","icn-line-star","icn-line-sun","icn-line-thermometer","icn-line-time","icn-line-trampoline","icn-line-trash-can","icn-line-tree","icn-line-waves","icn-line-youth","icn-linkedin","icn-list","icn-magnifying-glass","icn-map","icn-megaphone","icn-microphone","icn-minus","icn-money-circle","icn-mug","icn-night-activities","icn-notebook-pencil","icn-numbered-list","icn-pancakes","icn-pencil","icn-pencil-paper","icn-person","icn-phone","icn-pinterest","icn-pizza","icn-plate-setting","icn-plus","icn-pointer-hand","icn-question","icn-quiet-time","icn-radio-tower","icn-random-race","icn-refresh","icn-robot-confused","icn-robot-pizza","icn-rss","icn-sandwich","icn-scrap","icn-screen","icn-smartband","icn-sound","icn-star","icn-suitcase","icn-sun","icn-sunglasses","icn-sunrise","icn-switch-arrows","icn-tent","icn-texas","icn-theme-night","icn-thick-minus","icn-thick-plus","icn-thick-x","icn-thin-x","icn-thumbs-up","icn-trampoline","icn-triangle-down","icn-triangle-left","icn-triangle-right","icn-triangle-up","icn-tshirt","icn-turkey-dinner","icn-twitter-bird","icn-user","icn-user-boy","icn-user-girl","icn-user-group","icn-user-group-remove","icn-x","icn-youtube","icon-circle","icon-smaller1","icon-smaller2","icon-smaller3","icon-smaller4","icon-smaller5","ie7","ie8","image-link","img-hover-fade","inline","inline-block","inline-svg","inline-svg-indent","input-height","italictext","jqv-error","kern","labels-display-block","large-text-inputs","leadSuccessBox","like-h1","like-h2","like-h3","like-h4","like-h5","like-h6","line-height-0-0","line-height-0-1","line-height-0-2","line-height-0-3","line-height-0-4","line-height-0-5","line-height-0-6","line-height-0-7","line-height-0-8","line-height-0-9","line-height-1-0","line-height-1-1","line-height-1-2","line-height-1-3","line-height-1-4","line-height-1-5","line-height-1-6","line-height-1-7","line-height-1-8","line-height-1-9","line-height-2-0","line-height-2-1","line-height-2-2","line-height-2-3","line-height-2-4","line-height-2-5","line-height-2-6","line-height-2-7","line-height-2-8","line-height-2-9","lines-b","lines-h","lines-v","list-title","login-menu","loosen-left1","loosen-left10","loosen-left2","loosen-left3","loosen-left4","loosen-left5","loosen-left6","loosen-left7","loosen-left8","loosen-left9","loosen-right1","loosen-right10","loosen-right2","loosen-right3","loosen-right4","loosen-right5","loosen-right6","loosen-right7","loosen-right8","loosen-right9","map","menu-open","menu-toggle","mfp-arrow-left","mfp-arrow-right","mfp-b","mfp-bg","mfp-counter","mfp-figure","mfp-iframe-scaler","mfp-title","modal-window1","multi-line","nav-back-link","nav-bar-link","nav-button","nav-header","nav-header-container","nav-header-left","nav-header-login-area","nav-header-menu","nav-header-right","nav-header-spacer","nav-login","nav-login-utility-links","nav-logo","nav-menu-container","nav-overlay","nav-primary-links","nav-secondary-links-header","no-bottom-margin","no-margin","no-padding","no-scroll","no-underline","normaltext","normalweight","nowrap","nowrap-divs","nowrap-links","nowrap-spans","padbox","padbox-all-loose","padbox-all-none","padbox-all-normal","padbox-all-tight","padbox-all-xloose","padbox-all-xtight","padbox-all-xxloose","padbox-all-xxtight","padbox-bottom-loose","padbox-bottom-none","padbox-bottom-normal","padbox-bottom-tight","padbox-bottom-xloose","padbox-bottom-xtight","padbox-bottom-xxloose","padbox-bottom-xxtight","padbox-horiz-loose","padbox-horiz-none","padbox-horiz-normal","padbox-horiz-tight","padbox-horiz-xloose","padbox-horiz-xtight","padbox-horiz-xxloose","padbox-horiz-xxtight","padbox-left-loose","padbox-left-none","padbox-left-normal","padbox-left-tight","padbox-left-xloose","padbox-left-xtight","padbox-left-xxloose","padbox-left-xxtight","padbox-lg-all-loose","padbox-lg-all-none","padbox-lg-all-normal","padbox-lg-all-tight","padbox-lg-all-xloose","padbox-lg-all-xtight","padbox-lg-all-xxloose","padbox-lg-all-xxtight","padbox-lg-bottom-loose","padbox-lg-bottom-none","padbox-lg-bottom-normal","padbox-lg-bottom-tight","padbox-lg-bottom-xloose","padbox-lg-bottom-xtight","padbox-lg-bottom-xxloose","padbox-lg-bottom-xxtight","padbox-lg-horiz-loose","padbox-lg-horiz-none","padbox-lg-horiz-normal","padbox-lg-horiz-tight","padbox-lg-horiz-xloose","padbox-lg-horiz-xtight","padbox-lg-horiz-xxloose","padbox-lg-horiz-xxtight","padbox-lg-left-loose","padbox-lg-left-none","padbox-lg-left-normal","padbox-lg-left-tight","padbox-lg-left-xloose","padbox-lg-left-xtight","padbox-lg-left-xxloose","padbox-lg-left-xxtight","padbox-lg-notbottom-loose","padbox-lg-notbottom-none","padbox-lg-notbottom-normal","padbox-lg-notbottom-tight","padbox-lg-notbottom-xloose","padbox-lg-notbottom-xtight","padbox-lg-notbottom-xxloose","padbox-lg-notbottom-xxtight","padbox-lg-right-loose","padbox-lg-right-none","padbox-lg-right-normal","padbox-lg-right-tight","padbox-lg-right-xloose","padbox-lg-right-xtight","padbox-lg-right-xxloose","padbox-lg-right-xxtight","padbox-lg-top-loose","padbox-lg-top-none","padbox-lg-top-normal","padbox-lg-top-tight","padbox-lg-top-xloose","padbox-lg-top-xtight","padbox-lg-top-xxloose","padbox-lg-top-xxtight","padbox-lg-vert-loose","padbox-lg-vert-none","padbox-lg-vert-normal","padbox-lg-vert-tight","padbox-lg-vert-xloose","padbox-lg-vert-xtight","padbox-lg-vert-xxloose","padbox-lg-vert-xxtight","padbox-loose","padbox-md-all-loose","padbox-md-all-none","padbox-md-all-normal","padbox-md-all-tight","padbox-md-all-xloose","padbox-md-all-xtight","padbox-md-all-xxloose","padbox-md-all-xxtight","padbox-md-bottom-loose","padbox-md-bottom-none","padbox-md-bottom-normal","padbox-md-bottom-tight","padbox-md-bottom-xloose","padbox-md-bottom-xtight","padbox-md-bottom-xxloose","padbox-md-bottom-xxtight","padbox-md-horiz-loose","padbox-md-horiz-none","padbox-md-horiz-normal","padbox-md-horiz-tight","padbox-md-horiz-xloose","padbox-md-horiz-xtight","padbox-md-horiz-xxloose","padbox-md-horiz-xxtight","padbox-md-left-loose","padbox-md-left-none","padbox-md-left-normal","padbox-md-left-tight","padbox-md-left-xloose","padbox-md-left-xtight","padbox-md-left-xxloose","padbox-md-left-xxtight","padbox-md-notbottom-loose","padbox-md-notbottom-none","padbox-md-notbottom-normal","padbox-md-notbottom-tight","padbox-md-notbottom-xloose","padbox-md-notbottom-xtight","padbox-md-notbottom-xxloose","padbox-md-notbottom-xxtight","padbox-md-right-loose","padbox-md-right-none","padbox-md-right-normal","padbox-md-right-tight","padbox-md-right-xloose","padbox-md-right-xtight","padbox-md-right-xxloose","padbox-md-right-xxtight","padbox-md-top-loose","padbox-md-top-none","padbox-md-top-normal","padbox-md-top-tight","padbox-md-top-xloose","padbox-md-top-xtight","padbox-md-top-xxloose","padbox-md-top-xxtight","padbox-md-vert-loose","padbox-md-vert-none","padbox-md-vert-normal","padbox-md-vert-tight","padbox-md-vert-xloose","padbox-md-vert-xtight","padbox-md-vert-xxloose","padbox-md-vert-xxtight","padbox-no-bg","padbox-none","padbox-normal","padbox-notbottom-loose","padbox-notbottom-none","padbox-notbottom-normal","padbox-notbottom-tight","padbox-notbottom-xloose","padbox-notbottom-xtight","padbox-notbottom-xxloose","padbox-notbottom-xxtight","padbox-right-loose","padbox-right-none","padbox-right-normal","padbox-right-tight","padbox-right-xloose","padbox-right-xtight","padbox-right-xxloose","padbox-right-xxtight","padbox-sm-all-loose","padbox-sm-all-none","padbox-sm-all-normal","padbox-sm-all-tight","padbox-sm-all-xloose","padbox-sm-all-xtight","padbox-sm-all-xxloose","padbox-sm-all-xxtight","padbox-sm-bottom-loose","padbox-sm-bottom-none","padbox-sm-bottom-normal","padbox-sm-bottom-tight","padbox-sm-bottom-xloose","padbox-sm-bottom-xtight","padbox-sm-bottom-xxloose","padbox-sm-bottom-xxtight","padbox-sm-horiz-loose","padbox-sm-horiz-none","padbox-sm-horiz-normal","padbox-sm-horiz-tight","padbox-sm-horiz-xloose","padbox-sm-horiz-xtight","padbox-sm-horiz-xxloose","padbox-sm-horiz-xxtight","padbox-sm-left-loose","padbox-sm-left-none","padbox-sm-left-normal","padbox-sm-left-tight","padbox-sm-left-xloose","padbox-sm-left-xtight","padbox-sm-left-xxloose","padbox-sm-left-xxtight","padbox-sm-notbottom-loose","padbox-sm-notbottom-none","padbox-sm-notbottom-normal","padbox-sm-notbottom-tight","padbox-sm-notbottom-xloose","padbox-sm-notbottom-xtight","padbox-sm-notbottom-xxloose","padbox-sm-notbottom-xxtight","padbox-sm-right-loose","padbox-sm-right-none","padbox-sm-right-normal","padbox-sm-right-tight","padbox-sm-right-xloose","padbox-sm-right-xtight","padbox-sm-right-xxloose","padbox-sm-right-xxtight","padbox-sm-top-loose","padbox-sm-top-none","padbox-sm-top-normal","padbox-sm-top-tight","padbox-sm-top-xloose","padbox-sm-top-xtight","padbox-sm-top-xxloose","padbox-sm-top-xxtight","padbox-sm-vert-loose","padbox-sm-vert-none","padbox-sm-vert-normal","padbox-sm-vert-tight","padbox-sm-vert-xloose","padbox-sm-vert-xtight","padbox-sm-vert-xxloose","padbox-sm-vert-xxtight","padbox-tight","padbox-top-loose","padbox-top-none","padbox-top-normal","padbox-top-tight","padbox-top-xloose","padbox-top-xtight","padbox-top-xxloose","padbox-top-xxtight","padbox-vert-loose","padbox-vert-none","padbox-vert-normal","padbox-vert-tight","padbox-vert-xloose","padbox-vert-xtight","padbox-vert-xxloose","padbox-vert-xxtight","padbox-xloose","padbox-xs-all-loose","padbox-xs-all-none","padbox-xs-all-normal","padbox-xs-all-tight","padbox-xs-all-xloose","padbox-xs-all-xtight","padbox-xs-all-xxloose","padbox-xs-all-xxtight","padbox-xs-bottom-loose","padbox-xs-bottom-none","padbox-xs-bottom-normal","padbox-xs-bottom-tight","padbox-xs-bottom-xloose","padbox-xs-bottom-xtight","padbox-xs-bottom-xxloose","padbox-xs-bottom-xxtight","padbox-xs-horiz-loose","padbox-xs-horiz-none","padbox-xs-horiz-normal","padbox-xs-horiz-tight","padbox-xs-horiz-xloose","padbox-xs-horiz-xtight","padbox-xs-horiz-xxloose","padbox-xs-horiz-xxtight","padbox-xs-left-loose","padbox-xs-left-none","padbox-xs-left-normal","padbox-xs-left-tight","padbox-xs-left-xloose","padbox-xs-left-xtight","padbox-xs-left-xxloose","padbox-xs-left-xxtight","padbox-xs-notbottom-loose","padbox-xs-notbottom-none","padbox-xs-notbottom-normal","padbox-xs-notbottom-tight","padbox-xs-notbottom-xloose","padbox-xs-notbottom-xtight","padbox-xs-notbottom-xxloose","padbox-xs-notbottom-xxtight","padbox-xs-right-loose","padbox-xs-right-none","padbox-xs-right-normal","padbox-xs-right-tight","padbox-xs-right-xloose","padbox-xs-right-xtight","padbox-xs-right-xxloose","padbox-xs-right-xxtight","padbox-xs-top-loose","padbox-xs-top-none","padbox-xs-top-normal","padbox-xs-top-tight","padbox-xs-top-xloose","padbox-xs-top-xtight","padbox-xs-top-xxloose","padbox-xs-top-xxtight","padbox-xs-vert-loose","padbox-xs-vert-none","padbox-xs-vert-normal","padbox-xs-vert-tight","padbox-xs-vert-xloose","padbox-xs-vert-xtight","padbox-xs-vert-xxloose","padbox-xs-vert-xxtight","padbox-xtight","padbox-xxloose","padbox-xxtight","pc-nav-expanded","plus-link","pmeth-no-bg","pmeth-title-green","pmeth-wrapper","region","relative","remove-outer-children-margin","remove-outer-children-margin-accounting-for-inconsequential-parents-and-siblings","reset-list","right","royalSlider","rp-admin","rp-admin-hide","rsArrow","rsArrowDisabled","rsArrowIcn","rsArrowLeft","rsArrowRight","rsBullet","rsBullets","rsContent","rsGCaption","rsHor","rsNavSelected","rsOverflow","rsPCcarousel1","rsSlide","rsThumbs","rsVideoFrameHolder","select-match-input","setup-black","setup-white","shift-down0","shift-down1","shift-down10","shift-down15","shift-down2","shift-down20","shift-down3","shift-down4","shift-down5","shift-down6","shift-down7","shift-down8","shift-down9","shift-left0","shift-left1","shift-left10","shift-left15","shift-left2","shift-left20","shift-left3","shift-left4","shift-left5","shift-left6","shift-left7","shift-left8","shift-left9","shift-lg-down0","shift-lg-down1","shift-lg-down10","shift-lg-down15","shift-lg-down2","shift-lg-down20","shift-lg-down3","shift-lg-down4","shift-lg-down5","shift-lg-down6","shift-lg-down7","shift-lg-down8","shift-lg-down9","shift-lg-left0","shift-lg-left1","shift-lg-left10","shift-lg-left15","shift-lg-left2","shift-lg-left20","shift-lg-left3","shift-lg-left4","shift-lg-left5","shift-lg-left6","shift-lg-left7","shift-lg-left8","shift-lg-left9","shift-lg-right0","shift-lg-right1","shift-lg-right10","shift-lg-right15","shift-lg-right2","shift-lg-right20","shift-lg-right3","shift-lg-right4","shift-lg-right5","shift-lg-right6","shift-lg-right7","shift-lg-right8","shift-lg-right9","shift-lg-up0","shift-lg-up1","shift-lg-up10","shift-lg-up15","shift-lg-up2","shift-lg-up20","shift-lg-up3","shift-lg-up4","shift-lg-up5","shift-lg-up6","shift-lg-up7","shift-lg-up8","shift-lg-up9","shift-md-down0","shift-md-down1","shift-md-down10","shift-md-down15","shift-md-down2","shift-md-down20","shift-md-down3","shift-md-down4","shift-md-down5","shift-md-down6","shift-md-down7","shift-md-down8","shift-md-down9","shift-md-left0","shift-md-left1","shift-md-left10","shift-md-left15","shift-md-left2","shift-md-left20","shift-md-left3","shift-md-left4","shift-md-left5","shift-md-left6","shift-md-left7","shift-md-left8","shift-md-left9","shift-md-right0","shift-md-right1","shift-md-right10","shift-md-right15","shift-md-right2","shift-md-right20","shift-md-right3","shift-md-right4","shift-md-right5","shift-md-right6","shift-md-right7","shift-md-right8","shift-md-right9","shift-md-up0","shift-md-up1","shift-md-up10","shift-md-up15","shift-md-up2","shift-md-up20","shift-md-up3","shift-md-up4","shift-md-up5","shift-md-up6","shift-md-up7","shift-md-up8","shift-md-up9","shift-right0","shift-right1","shift-right10","shift-right15","shift-right2","shift-right20","shift-right3","shift-right4","shift-right5","shift-right6","shift-right7","shift-right8","shift-right9","shift-sm-down0","shift-sm-down1","shift-sm-down10","shift-sm-down15","shift-sm-down2","shift-sm-down20","shift-sm-down3","shift-sm-down4","shift-sm-down5","shift-sm-down6","shift-sm-down7","shift-sm-down8","shift-sm-down9","shift-sm-left0","shift-sm-left1","shift-sm-left10","shift-sm-left15","shift-sm-left2","shift-sm-left20","shift-sm-left3","shift-sm-left4","shift-sm-left5","shift-sm-left6","shift-sm-left7","shift-sm-left8","shift-sm-left9","shift-sm-right0","shift-sm-right1","shift-sm-right10","shift-sm-right15","shift-sm-right2","shift-sm-right20","shift-sm-right3","shift-sm-right4","shift-sm-right5","shift-sm-right6","shift-sm-right7","shift-sm-right8","shift-sm-right9","shift-sm-up0","shift-sm-up1","shift-sm-up10","shift-sm-up15","shift-sm-up2","shift-sm-up20","shift-sm-up3","shift-sm-up4","shift-sm-up5","shift-sm-up6","shift-sm-up7","shift-sm-up8","shift-sm-up9","shift-up0","shift-up1","shift-up10","shift-up15","shift-up2","shift-up20","shift-up3","shift-up4","shift-up5","shift-up6","shift-up7","shift-up8","shift-up9","shift-xs-down0","shift-xs-down1","shift-xs-down10","shift-xs-down15","shift-xs-down2","shift-xs-down20","shift-xs-down3","shift-xs-down4","shift-xs-down5","shift-xs-down6","shift-xs-down7","shift-xs-down8","shift-xs-down9","shift-xs-left0","shift-xs-left1","shift-xs-left10","shift-xs-left15","shift-xs-left2","shift-xs-left20","shift-xs-left3","shift-xs-left4","shift-xs-left5","shift-xs-left6","shift-xs-left7","shift-xs-left8","shift-xs-left9","shift-xs-right0","shift-xs-right1","shift-xs-right10","shift-xs-right15","shift-xs-right2","shift-xs-right20","shift-xs-right3","shift-xs-right4","shift-xs-right5","shift-xs-right6","shift-xs-right7","shift-xs-right8","shift-xs-right9","shift-xs-up0","shift-xs-up1","shift-xs-up10","shift-xs-up15","shift-xs-up2","shift-xs-up20","shift-xs-up3","shift-xs-up4","shift-xs-up5","shift-xs-up6","shift-xs-up7","shift-xs-up8","shift-xs-up9","slide-caption1","slide-caption1-heading","slide-caption1-paragraph","slide-caption1-text","small","small-adjust-hide","small-adjust-lg-up","small-adjust-md-only","small-adjust-md-up","small-adjust-sm-only","small-adjust-sm-up","small-heading","smooth-font","spacer","spacer-lg-loose","spacer-lg-none","spacer-lg-normal","spacer-lg-tight","spacer-lg-xloose","spacer-lg-xtight","spacer-lg-xxloose","spacer-lg-xxtight","spacer-loose","spacer-md-loose","spacer-md-none","spacer-md-normal","spacer-md-tight","spacer-md-xloose","spacer-md-xtight","spacer-md-xxloose","spacer-md-xxtight","spacer-none","spacer-normal","spacer-sm-loose","spacer-sm-none","spacer-sm-normal","spacer-sm-tight","spacer-sm-xloose","spacer-sm-xtight","spacer-sm-xxloose","spacer-sm-xxtight","spacer-tight","spacer-xloose","spacer-xs-loose","spacer-xs-none","spacer-xs-normal","spacer-xs-tight","spacer-xs-xloose","spacer-xs-xtight","spacer-xs-xxloose","spacer-xs-xxtight","spacer-xtight","spacer-xxloose","spacer-xxtight","svg-fill-container","tab-active","tab-content","tab-handle","tab-set","tel-link","text-plus-select","tighten-left1","tighten-left10","tighten-left2","tighten-left3","tighten-left4","tighten-left5","tighten-left6","tighten-left7","tighten-left8","tighten-left9","tighten-right1","tighten-right10","tighten-right2","tighten-right3","tighten-right4","tighten-right5","tighten-right6","tighten-right7","tighten-right8","tighten-right9","titlecase-text","tpad-loose","tpad-none","tpad-normal","tpad-tight","tpad-xloose","tpad-xtight","tpad-xxloose","tpad-xxtight","tps-focus","tps-no-border","tps-select","tps-text","tps-text-prefix","translate-center-v","translate-center-v-h","truncate","underline","underlined","unsmooth-font","uppercase","video-overlay-button","visible-lg-down","visible-lg-down-inline","visible-lg-down-inline-block","visible-lg-only","visible-lg-only-inline","visible-lg-only-inline-block","visible-lg-up","visible-lg-up-inline","visible-lg-up-inline-block","visible-md-down","visible-md-down-inline","visible-md-down-inline-block","visible-md-only","visible-md-only-inline","visible-md-only-inline-block","visible-md-up","visible-md-up-inline","visible-md-up-inline-block","visible-sm-down","visible-sm-down-inline","visible-sm-down-inline-block","visible-sm-only","visible-sm-only-inline","visible-sm-only-inline-block","visible-sm-up","visible-sm-up-inline","visible-sm-up-inline-block","visible-xs-down","visible-xs-down-inline","visible-xs-down-inline-block","visible-xs-only","visible-xs-only-inline","visible-xs-only-inline-block","visible-xs-up","visible-xs-up-inline","visible-xs-up-inline-block","visually-hidden","width-10","width-100","width-100percent","width-120","width-140","width-160","width-180","width-20","width-200","width-30","width-40","width-50","width-60","width-70","width-80","width-90","width-auto","width-lg-10","width-lg-100","width-lg-100percent","width-lg-120","width-lg-140","width-lg-160","width-lg-180","width-lg-20","width-lg-200","width-lg-30","width-lg-40","width-lg-50","width-lg-60","width-lg-70","width-lg-80","width-lg-90","width-lg-auto","width-md-10","width-md-100","width-md-100percent","width-md-120","width-md-140","width-md-160","width-md-180","width-md-20","width-md-200","width-md-30","width-md-40","width-md-50","width-md-60","width-md-70","width-md-80","width-md-90","width-md-auto","width-sm-10","width-sm-100","width-sm-100percent","width-sm-120","width-sm-140","width-sm-160","width-sm-180","width-sm-20","width-sm-200","width-sm-30","width-sm-40","width-sm-50","width-sm-60","width-sm-70","width-sm-80","width-sm-90","width-sm-auto","width-xs-10","width-xs-100","width-xs-100percent","width-xs-120","width-xs-140","width-xs-160","width-xs-180","width-xs-20","width-xs-200","width-xs-30","width-xs-40","width-xs-50","width-xs-60","width-xs-70","width-xs-80","width-xs-90","width-xs-auto","wp-caption","wrapper","x_fitText"]



class Style4Completions(sublime_plugin.EventListener):
    """
    Provide tag completions for Style4 elements and data-uk attributes
    """
    def __init__(self):

        self.class_completions = [("%s \tPC Style4 Class" % s, s) for s in style4_classes]

    def on_query_completions(self, view, prefix, locations):

        if view.match_selector(locations[0], "text.html string.quoted"):

            # Cursor is inside a quoted attribute
            # Now check if we are inside the class attribute

            # max search size
            LIMIT  = 250

            # place search cursor one word back
            cursor = locations[0] - len(prefix) - 1

            # dont start with negative value
            start  = max(0, cursor - LIMIT - len(prefix))

            # get part of buffer
            line   = view.substr(sublime.Region(start, cursor))

            # split attributes
            parts  = line.split('=')

            # is the last typed attribute a class attribute?
            if len(parts) > 1 and parts[-2].strip().endswith("class"):
                return self.class_completions
            else:
                return []
        elif view.match_selector(locations[0], "text.html meta.tag - text.html punctuation.definition.tag.begin"):

            # Cursor is in a tag, but not inside an attribute, i.e. <div {here}>
            # This one is easy, just return completions for the data-uk-* attributes
            return self.data_completions

        else:

            return []