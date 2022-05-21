(function($) {
    'use strict';

    /**
    * Pages.
     * @constructor
     * @property {string}  VERSION      - Build Version.
     * @property {string}  AUTHOR       - Author.
     * @property {string}  SUPPORT      - Support Email.
     * @property {string}  pageScrollElement  - Scroll Element in Page.
     * @property {object}  $body - Cache Body.
     */
    var Pages = function() {
        this.VERSION = "1.0.0";
        this.AUTHOR = "";
        this.SUPPORT = "";

        this.pageScrollElement = 'html, body';
        this.$body = $('body');

        this.setUserOS();
        this.setUserAgent();
    }

    /** @function setUserOS
    * @description SET User Operating System eg: mac,windows,etc
    * @returns {string} - Appends OSName to Pages.$body
    */
    Pages.prototype.setUserOS = function() {
        var OSName = "";
        if (navigator.appVersion.indexOf("Win") != -1) OSName = "windows";
        if (navigator.appVersion.indexOf("Mac") != -1) OSName = "mac";
        if (navigator.appVersion.indexOf("X11") != -1) OSName = "unix";
        if (navigator.appVersion.indexOf("Linux") != -1) OSName = "linux";

        this.$body.addClass(OSName);
    }

    /** @function setUserAgent
    * @description SET User Device Name to mobile | desktop
    * @returns {string} - Appends Device to Pages.$body
    */
    Pages.prototype.setUserAgent = function() {
        if (navigator.userAgent.match(/Android|BlackBerry|iPhone|iPad|iPod|Opera Mini|IEMobile/i)) {
            this.$body.addClass('mobile');
        } else {
            this.$body.addClass('desktop');
            if (navigator.userAgent.match(/MSIE 9.0/)) {
                this.$body.addClass('ie9');
            }
        }
    }

    /** @function isVisibleXs
    * @description Checks if the screen size is XS - Extra Small i.e below W480px
    * @returns {$Element} - Appends $('#pg-visible-xs') to Body
    */
    Pages.prototype.isVisibleXs = function() {
        (!$('#pg-visible-xs').length) && this.$body.append('<div id="pg-visible-xs" class="visible-xs" />');
        return $('#pg-visible-xs').is(':visible');
    }

    /** @function isVisibleSm
    * @description Checks if the screen size is SM - Small Screen i.e Above W480px
    * @returns {$Element} - Appends $('#pg-visible-sm') to Body
    */
    Pages.prototype.isVisibleSm = function() {
        (!$('#pg-visible-sm').length) && this.$body.append('<div id="pg-visible-sm" class="visible-sm" />');
        return $('#pg-visible-sm').is(':visible');
    }

    /** @function isVisibleMd
    * @description Checks if the screen size is MD - Medium Screen i.e Above W1024px
    * @returns {$Element} - Appends $('#pg-visible-md') to Body
    */
    Pages.prototype.isVisibleMd = function() {
        (!$('#pg-visible-md').length) && this.$body.append('<div id="pg-visible-md" class="visible-md" />');
        return $('#pg-visible-md').is(':visible');
    }

    /** @function isVisibleLg
    * @description Checks if the screen size is LG - Large Screen i.e Above W1200px
    * @returns {$Element} - Appends $('#pg-visible-lg') to Body
    */
    Pages.prototype.isVisibleLg = function() {
        (!$('#pg-visible-lg').length) && this.$body.append('<div id="pg-visible-lg" class="visible-lg" />');
        return $('#pg-visible-lg').is(':visible');
    }

    /** @function getUserAgent
    * @description Get Current User Agent.
    * @returns {string} - mobile | desktop
    */
    Pages.prototype.getUserAgent = function() {
        return $('body').hasClass('mobile') ? "mobile" : "desktop";
    }

    /** @function setFullScreen
    * @description Make Browser fullscreen.
    */
    Pages.prototype.setFullScreen = function(element) {
        // Supports most browsers and their versions.
        var requestMethod = element.requestFullScreen || element.webkitRequestFullScreen || element.mozRequestFullScreen || element.msRequestFullscreen;

        if (requestMethod) { // Native full screen.
            requestMethod.call(element);
        } else if (typeof window.ActiveXObject !== "undefined") { // Older IE.
            var wscript = new ActiveXObject("WScript.Shell");
            if (wscript !== null) {
                wscript.SendKeys("{F11}");
            }
        }
    }

    /** @function getColor
    * @description Get Color from CSS
    * @param {string} color - pages color class eg: primary,master,master-light etc.
    * @param {int} opacity
    * @returns {rgba}
    */
    Pages.prototype.getColor = function(color, opacity) {
        opacity = parseFloat(opacity) || 1;

        var elem = $('.pg-colors').length ? $('.pg-colors') : $('<div class="pg-colors"></div>').appendTo('body');

        var colorElem = elem.find('[data-color="' + color + '"]').length ? elem.find('[data-color="' + color + '"]') : $('<div class="bg-' + color + '" data-color="' + color + '"></div>').appendTo(elem);

        var color = colorElem.css('background-color');

        var rgb = color.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
        var rgba = "rgba(" + rgb[1] + ", " + rgb[2] + ", " + rgb[3] + ', ' + opacity + ')';

        return rgba;
    }

    /** @function initSidebar
    * @description Initialize side bar to open and close
    * @param {(Element|JQuery)} [context] - A DOM Element, Document, or jQuery to use as context.
    * @requires ui/sidebar.js
    */
    Pages.prototype.initSidebar = function(context) {
        $('[data-pages="sidebar"]', context).each(function() {
            var $sidebar = $(this)
            $sidebar.sidebar($sidebar.data())
        })
    }

    /** @function initFormGroupDefault
    * @description Initialize Pages form group input
    * @param {(Element|JQuery)} [context] - A DOM Element, Document, or jQuery to use as context.
    */
    Pages.prototype.initFormGroupDefault = function(context) {
        $('.form-group.form-group-default', context).click(function() {
            $(this).find('input').focus();
        });

        if (!this.initFormGroupDefaultRun) {
            $('body').on('focus', '.form-group.form-group-default :input', function() {
                $('.form-group.form-group-default').removeClass('focused');
                $(this).parents('.form-group').addClass('focused');
            });

            $('body').on('blur', '.form-group.form-group-default :input', function() {
                $(this).parents('.form-group').removeClass('focused');
                if ($(this).val()) {
                    $(this).closest('.form-group').find('label').addClass('fade');
                } else {
                    $(this).closest('.form-group').find('label').removeClass('fade');
                }
            });

            // Only run the above code once.
            this.initFormGroupDefaultRun = true;
        }

        $('.form-group.form-group-default .checkbox, .form-group.form-group-default .radio', context).hover(function() {
            $(this).parents('.form-group').addClass('focused');
        }, function() {
            $(this).parents('.form-group').removeClass('focused');
        });
    }

    /** @function initProgressBars
    * @description Initialize Pages ProgressBars
    */
    Pages.prototype.initProgressBars = function() {
        $(window).on('load', function() {
            // Hack: FF doesn't play SVG animations set as background-image
            $('.progress-bar-indeterminate, .progress-circle-indeterminate, .mapplic-pin').hide().show(0);
        });
    }

    /** @function initInputFile
    * @description Initialize File Input for Bootstrap Buttons and Input groups
    */
    Pages.prototype.initInputFile = function() {
        $(document).on('change', '.btn-file :file', function() {
            var input = $(this),
            numFiles = input.get(0).files ? input.get(0).files.length : 1,
            label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
            input.trigger('fileselect', [numFiles, label]);
        });

        $('.btn-file :file').on('fileselect', function(event, numFiles, label) {
            var input = $(this).parents('.input-group').find(':text'),
                log = numFiles > 1 ? numFiles + ' files selected' : label;
            if( input.length ) {
                input.val(log);
            } else {
                $(this).parent().html(log);
            }
        });
    }
    /** @function initHorizontalMenu
    * @description Initialize Horizontal Dropdown Menu
    */
    Pages.prototype.initHorizontalMenu = function(){
        var animationTimer;

        var hMenu = $("[data-pages-init='horizontal-menu']");
        autoHideLi();
        $(document).on('click', '.menu-bar > ul > li', function(){
            if($(this).children("ul").length == 0){
                return;
            }
            if($(window).width() < 992) {
              var menubar = $('.menu-bar');
              var el = $(this);
              var li = menubar.find('li');
              var sub = $(this).children('ul');

              if(el.hasClass("open active")){
                 el.find('.arrow').removeClass("open active");
                 sub.slideUp(200, function() {
                     el.removeClass("open active");
                 });

              }else{
                 menubar.find('li.open').find('ul').slideUp(200);
                 menubar.find('li.open').find('a').find('.arrow').removeClass('open active');
                 menubar.find('li.open').removeClass("open active");
                 el.find('.arrow').addClass("open active");
                 sub.slideDown(200, function() {
                     el.addClass("open active");
                 });
              }
            } else {
              if($(this).hasClass('opening')){
                   _hideMenu($(this));
              }
              else{
                  _showMenu($(this));
              }
            }

        });

        var resizeTimer;
        $(window).on('resize', function(e) {
          clearTimeout(resizeTimer);
          resizeTimer = setTimeout(function() {
            autoHideLi();
          }, 250);
        });

        $('.content').on('click', function () {
            $('.horizontal-menu .bar-inner > ul > li').removeClass('open');
            $('.menu-bar > ul > li').removeClass('open opening').children("ul").removeAttr("style");
            $("body").find(".ghost-nav-dropdown").remove();
        });

        $('[data-toggle="horizontal-menu"]').on('click touchstart', function(e) {
            e.preventDefault();
            $('body').toggleClass('horizontal-menu-open');
            if(!$('.horizontal-menu-backdrop').length){
              $('.header').append('<div class="horizontal-menu-backdrop"/>');
              $('.horizontal-menu-backdrop').fadeToggle('fast');
            } else {
              $('.horizontal-menu-backdrop').fadeToggle('fast', function(){
                $(this).remove();
              });
            }

            $('.menu-bar').toggleClass('open');
        });

        function autoHideLi(){
            var hMenu  = $("[data-pages-init='horizontal-menu']");
            var extraLiHide = parseInt(hMenu.data("hideExtraLi")) || 0
            if(hMenu.length == 0){
                return
            }
            var hMenuRect = hMenu[0].getBoundingClientRect();
            var liTotalWidth = 0;
            var liCount = 0;
            hMenu.children('ul').children('li.more').remove();
            hMenu.children('ul').children('li').each(function( index ) {
                $(this).removeAttr("style");
                liTotalWidth = liTotalWidth + $(this).outerWidth(true);
                liCount++;
            });

            if($(window).width() < 992) {
              return;
            }

            var possibleLi = parseInt(hMenuRect.width / (liTotalWidth / liCount)) - 1;
            possibleLi = possibleLi - extraLiHide;

            if(liCount > possibleLi){
                var wrapper = createWrapperLI(hMenu);
                for(var i = possibleLi; i < liCount; i++){
                    var currentLi = hMenu.children('ul').children('li').eq(i);
                    var clone = currentLi.clone();
                    clone.children("ul").addClass("sub-menu");
                    wrapper.children("ul").append(clone);
                    currentLi.hide();
                }
            }

        }

        function createWrapperLI(hMenu){
            var li =hMenu.children('ul').append("<li class='more'><a href='javascript:;'><span class='title'><i class='pg pg-more'></i></span></a><ul></ul></li>");
            li = hMenu.children('ul').children('li.more');
            return li;
        }

        function _hideMenu($el){
            var ul  = $($el.children("ul")[0]);
            var ghost = $("<div class='ghost-nav-dropdown'></div>");
            if(ul.length == 0){
                return;
            }
            var rect = ul[0].getBoundingClientRect();
            ghost.css({
                "width":rect.width+"px",
                "height":rect.height+"px",
                "z-index":"auto"
            })
            $el.append(ghost);
            var timingSpeed = ul.children("li").css('transition-duration');

            timingSpeed = parseInt(parseFloat(timingSpeed) * 1000);
            $el.addClass('closing');
            window.clearTimeout(animationTimer);
            animationTimer = window.setTimeout(function(){
                ghost.height(0);
                $el.removeClass('open opening closing');
            },timingSpeed - 80);
        }
        function _showMenu($el){

            var ul  = $($el.children("ul")[0]);
            var ghost = $("<div class='ghost-nav-dropdown'></div>");
            $el.children(".ghost-nav-dropdown").remove();
            $el.addClass('open').siblings().removeClass('open opening');
            if(ul.length == 0){
                return;
            }
            var rect = ul[0].getBoundingClientRect();
            ghost.css({
                "width":rect.width+"px",
                "height":"0px"
            });
            $el.append(ghost);
            ghost.height(rect.height);
            var timingSpeed = ghost.css('transition-duration');

            timingSpeed = parseInt(parseFloat(timingSpeed) * 1000)
            window.clearTimeout(animationTimer);
            animationTimer = window.setTimeout(function(){
                $el.addClass('opening');
                ghost.remove()
            },timingSpeed);
        }
    }
    /** @function initTooltipPlugin
    * @description Initialize Bootstrap tooltip
    * @param {(Element|JQuery)} [context] - A DOM Element, Document, or jQuery to use as context.
    * @requires bootstrap.js
    */
    Pages.prototype.initTooltipPlugin = function(context) {
        $.fn.tooltip && $('[data-toggle="tooltip"]', context).tooltip();
    }
    /** @function initSelect2Plugin
    * @description Initialize select2 dropdown
    * @param {(Element|JQuery)} [context] - A DOM Element, Document, or jQuery to use as context.
    * @requires select2.js version 4.0.x
    */
    Pages.prototype.initSelect2Plugin = function(context) {
        $.fn.select2 && $('[data-init-plugin="select2"]', context).each(function() {
            $(this).select2({
                minimumResultsForSearch: ($(this).attr('data-disable-search') == 'true' ? -1 : 1)
            }).on('select2:open', function() {
                $.fn.scrollbar && $('.select2-results__options').scrollbar({
                    ignoreMobile: false
                })
            });
        });
    }
    /** @function initScrollBarPlugin
    * @description Initialize Global Scroller
    * @param {(Element|JQuery)} [context] - A DOM Element, Document, or jQuery to use as context.
    * @requires jquery-scrollbar.js
    */
    Pages.prototype.initScrollBarPlugin = function(context) {
        $.fn.scrollbar && $('.scrollable', context).scrollbar({
            ignoreOverlay: false
        });
    }
    /** @function initListView
    * @description Initialize iOS like List view plugin
    * @param {(Element|JQuery)} [context] - A DOM Element, Document, or jQuery to use as context.
    * @example <caption>data-init-list-view="ioslist"</caption>
    * @requires jquery-ioslist.js
    */
    Pages.prototype.initListView = function(context) {
        $.fn.ioslist && $('[data-init-list-view="ioslist"]', context).ioslist();
        $.fn.scrollbar && $('.list-view-wrapper', context).scrollbar({
            ignoreOverlay: false
        });
    }

    /** @function initSwitcheryPlugin
    * @description Initialize iOS like List view plugin
    * @param {(Element|JQuery)} [context] - A DOM Element, Document, or jQuery to use as context.
    * @example <caption>data-init-plugin="switchery"</caption>
    * @requires Switchery.js
    */
    Pages.prototype.initSwitcheryPlugin = function(context) {
        // Switchery - ios7 switch
        window.Switchery && $('[data-init-plugin="switchery"]', context).each(function() {
            var el = $(this);
            new Switchery(el.get(0), {
                color: (el.data("color") != null ?  $.Pages.getColor(el.data("color")) : $.Pages.getColor('success')),
                size : (el.data("size") != null ?  el.data("size") : "default")
            });
        });
    }

    /** @function initUnveilPlugin
    * @description To load retina images to img tag
    * @param {(Element|JQuery)} [context] - A DOM Element, Document, or jQuery to use as context.
    */
    Pages.prototype.initUnveilPlugin = function(context) {
        // lazy load retina images
        $.fn.unveil && $("img", context).unveil();
    }

    /** @function initValidatorPlugin
    * @description Inintialize and Overide exsisting jquery-validate methods.
    * @requires jquery-validate.js
    */
    Pages.prototype.initValidatorPlugin = function() {
        /**
         * Open the socket.
         * @override
         */
        $.validator && $.validator.setDefaults({
            ignore: "", // validate hidden fields, required for cs-select
            showErrors: function(errorMap, errorList) {
                var $this = this;
                $.each(this.successList, function(index, value) {
                    var parent = $(this).closest('.form-group-attached');
                    if (parent.length) return $(value).popover("hide");
                });
                return $.each(errorList, function(index, value) {

                    var parent = $(value.element).closest('.form-group-attached');
                    if (!parent.length) {
                        return $this.defaultShowErrors();
                    }
                    var _popover;
                    _popover = $(value.element).popover({
                        trigger: "manual",
                        placement: "top",
                        html: true,
                        container: parent.closest('form'),
                        content: value.message
                    });
                    var parent = $(value.element).closest('.form-group');
                    parent.addClass('has-error');
                    $(value.element).popover("show");
                });
            },
            onfocusout: function(element) {
                var parent = $(element).closest('.form-group');
                if ($(element).valid()) {
                    parent.removeClass('has-error');
                    parent.next('.error').remove();
                }
            },
            onkeyup: function(element) {
                var parent = $(element).closest('.form-group');
                if ($(element).valid()) {
                    $(element).removeClass('error');
                    parent.removeClass('has-error');
                    parent.next('label.error').remove();
                    parent.find('label.error').remove();
                } else {
                    parent.addClass('has-error');
                }
            },
            errorPlacement: function(error, element) {
                var parent = $(element).closest('.form-group');
                if (parent.hasClass('form-group-default')) {
                    parent.addClass('has-error');
                    error.insertAfter(parent);
                } else if(element.parent().hasClass('checkbox')) {
                    error.insertAfter(element.parent());
                } else {
                    error.insertAfter(element);
                }
            }
        });
    }

    /** @function setBackgroundImage
    * @description load images to div using data API
    */
    Pages.prototype.setBackgroundImage = function() {
        $('[data-pages-bg-image]').each(function() {
            var _elem = $(this)
            var defaults = {
                pagesBgImage: "",
                lazyLoad: 'true',
                progressType: '',
                progressColor:'',
                bgOverlay:'',
                bgOverlayClass:'',
                overlayOpacity:0,
            }
            var data = _elem.data();
            $.extend( defaults, data );
            var url = defaults.pagesBgImage;
            var color = defaults.bgOverlay;
            var opacity = defaults.overlayOpacity;

            var overlay = $('<div class="bg-overlay"></div>');
            overlay.addClass(defaults.bgOverlayClass);
            overlay.css({
                'background-color': color,
                'opacity': 1
            });
            _elem.append(overlay);

            var img = new Image();
            img.src = url;
            img.onload = function(){
                _elem.css({
                    'background-image': 'url(' + url + ')'
                });
                _elem.children('.bg-overlay').css({'opacity': opacity});
            }

        })
    }
    /** @function init
    * @description Inintialize all core components.
    */
    Pages.prototype.init = function() {
        // init layout
        this.initSidebar();
        this.setBackgroundImage();
        this.initFormGroupDefault();
        this.initProgressBars();
        this.initHorizontalMenu();
        // init plugins
        this.initTooltipPlugin();
        this.initSelect2Plugin();
        this.initScrollBarPlugin();
        this.initSwitcheryPlugin();
        this.initUnveilPlugin();
        this.initValidatorPlugin();
        this.initListView();
        this.initInputFile();
    }

    $.Pages = new Pages();
    $.Pages.Constructor = Pages;

})(window.jQuery);

/* ============================================================
 * Pages Circular Progress
 * ============================================================ */

(function($) {
    'use strict';
    // CIRCULAR PROGRESS CLASS DEFINITION
    // ======================

    var Progress = function(element, options) {
        this.$element = $(element);
        this.options = $.extend(true, {}, $.fn.circularProgress.defaults, options);


        // start adding to to DOM
        this.$container = $('<div class="progress-circle"></div>');

        this.$element.attr('data-color') && this.$container.addClass('progress-circle-' + this.$element.attr('data-color'));
        this.$element.attr('data-thick') && this.$container.addClass('progress-circle-thick');

        this.$pie = $('<div class="pie"></div>');

        this.$pie.$left = $('<div class="left-side half-circle"></div>');
        this.$pie.$right = $('<div class="right-side half-circle"></div>');

        this.$pie.append(this.$pie.$left).append(this.$pie.$right);

        this.$container.append(this.$pie).append('<div class="shadow"></div>');

        this.$element.after(this.$container);
        // end DOM adding

        this.val = this.$element.val();
        var deg = perc2deg(this.val);


        if (this.val <= 50) {
            this.$pie.$right.css('transform', 'rotate(' + deg + 'deg)');
        } else {
            this.$pie.css('clip', 'rect(auto, auto, auto, auto)');
            this.$pie.$right.css('transform', 'rotate(180deg)');
            this.$pie.$left.css('transform', 'rotate(' + deg + 'deg)');
        }

    }
    Progress.VERSION = "1.0.0";

    Progress.prototype.value = function(val) {
        if (typeof val == 'undefined') return;

        var deg = perc2deg(val);

        this.$pie.removeAttr('style');

        this.$pie.$right.removeAttr('style');
        this.$pie.$left.removeAttr('style');

        if (val <= 50) {
            this.$pie.$right.css('transform', 'rotate(' + deg + 'deg)');
        } else {
            this.$pie.css('clip', 'rect(auto, auto, auto, auto)');
            this.$pie.$right.css('transform', 'rotate(180deg)');
            this.$pie.$left.css('transform', 'rotate(' + deg + 'deg)');
        }

    }

    // CIRCULAR PROGRESS PLUGIN DEFINITION
    // =======================
    function Plugin(option) {
        return this.filter(':input').each(function() {
            var $this = $(this);
            var data = $this.data('pg.circularProgress');
            var options = typeof option == 'object' && option;

            if (!data) $this.data('pg.circularProgress', (data = new Progress(this, options)));
            if (typeof option == 'string') data[option]();
            else if (options.hasOwnProperty('value')) data.value(options.value);
        })
    }

    var old = $.fn.circularProgress

    $.fn.circularProgress = Plugin
    $.fn.circularProgress.Constructor = Progress


    $.fn.circularProgress.defaults = {
        value: 0
    }

    // CIRCULAR PROGRESS NO CONFLICT
    // ====================

    $.fn.circularProgress.noConflict = function() {
        $.fn.circularProgress = old;
        return this;
    }

    // CIRCULAR PROGRESS DATA API
    //===================

    $(window).on('load', function() {
        $('[data-pages-progress="circle"]').each(function() {
            var $progress = $(this)
            $progress.circularProgress($progress.data())
        })
    })

    function perc2deg(p) {
        return parseInt(p / 100 * 360);
    }

    // TODO: Add API to change size, stroke width, color

})(window.jQuery);

/* ============================================================
 * Pages Mobile View
 * ============================================================ */
(function($) {
    'use strict';

    var MobileView = function(element, options) {
        var self = this;
        self.options = $.extend(true, {}, $.fn.pgMobileViews.defaults, options);
        self.element = $(element);
        self.element.on('click', function(e) {
            e.preventDefault();
            var data = self.element.data();
            var el = $(data.viewPort);
            var toView = data.toggleView;
            if (data.toggleView != null) {
                el.children().last().children('.view').hide();
                $(data.toggleView).show();
            }
            else{
                 toView = el.last();
            }
            el.toggleClass(data.viewAnimation);
            self.options.onNavigate(toView, data.viewAnimation);
            return false;
        })
        return this; // enable chaining
    };
    $.fn.pgMobileViews = function(options) {
        return new MobileView(this, options);
    };

    $.fn.pgMobileViews.defaults = {
        //Returns Target View & Animation Type
        onNavigate: function(view, animation) {}
    }
    // MOBILE VIEW DATA API
    //===================

    $(window).on('load', function() {
        $('[data-navigate="view"]').each(function() {
            var $mobileView = $(this)
            $mobileView.pgMobileViews();
        })
    });
})(window.jQuery);


 /* ============================================================
  * Pages Sidebar
  * ============================================================ */

 (function($) {
    'use strict';
     // SIDEBAR CLASS DEFINITION
     // ======================

    var Sidebar = function(element, options) {
         this.$element = $(element);
         this.$body = $('body');
         this.options = $.extend(true, {}, $.fn.sidebar.defaults, options);

         this.bezierEasing = [.05, .74, .27, .99];
         this.cssAnimation = true;
         this.css3d = true;

         this.sideBarWidth = 280;
         this.sideBarWidthCondensed = 280 - 70;



         this.$sidebarMenu = this.$element.find('.sidebar-menu > ul');
         this.$pageContainer = $(this.options.pageContainer);


         if (!this.$sidebarMenu.length) return;

         // apply perfectScrollbar plugin only for desktops
         ($.Pages.getUserAgent() == 'desktop') && this.$sidebarMenu.scrollbar({
             ignoreOverlay: false,
             disableBodyScroll :(this.$element.data("disableBodyScroll") == true)? true : false
         });


         if (!Modernizr.csstransitions)
             this.cssAnimation = false;
         if (!Modernizr.csstransforms3d)
             this.css3d = false;

         // Bind events
         // Toggle sub menus
         // In Angular Binding is done using a pg-sidebar directive
         (typeof angular === 'undefined') && $(document).on('click', '.sidebar-menu a', function(e) {

             if ($(this).parent().children('.sub-menu') === false) {
                 return;
             }
             var el = $(this);
             var parent = $(this).parent().parent();
             var li = $(this).parent();
             var sub = $(this).parent().children('.sub-menu');

             if(li.hasClass("open active")){
                el.children('.arrow').removeClass("open active");
                sub.slideUp(200, function() {
                    li.removeClass("open active");
                });

             }else{
                parent.children('li.open').children('.sub-menu').slideUp(200);
                parent.children('li.open').children('a').children('.arrow').removeClass('open active');
                parent.children('li.open').removeClass("open active");
                el.children('.arrow').addClass("open active");
                sub.slideDown(200, function() {
                    li.addClass("open active");

                });
             }
             //e.preventDefault();
         });

         // Toggle sidebar
         $('.sidebar-slide-toggle').on('click touchend', function(e) {
             e.preventDefault();
             $(this).toggleClass('active');
             var el = $(this).attr('data-pages-toggle');
             if (el != null) {
                 $(el).toggleClass('show');
             }
         });

         var _this = this;

         function sidebarMouseEnter(e) {
            var _sideBarWidthCondensed = _this.$body.hasClass("rtl") ? -_this.sideBarWidthCondensed : _this.sideBarWidthCondensed;

             var menuOpenCSS = (this.css3d == true ? 'translate3d(' + _sideBarWidthCondensed + 'px, 0,0)' : 'translate(' + _sideBarWidthCondensed + 'px, 0)');

             if ($.Pages.isVisibleSm() || $.Pages.isVisibleXs()) {
                 return false
             }
             if ($('.close-sidebar').data('clicked')) {
                 return;
             }
             if (_this.$body.hasClass('menu-pin'))
                 return;

             _this.$element.css({
                 'transform': menuOpenCSS
             });
             _this.$body.addClass('sidebar-visible');
         }

         function sidebarMouseLeave(e) {
            var menuClosedCSS = (_this.css3d == true ? 'translate3d(0, 0,0)' : 'translate(0, 0)');

             if ($.Pages.isVisibleSm() || $.Pages.isVisibleXs()) {
                 return false
             }
             if (typeof e != 'undefined') {
                 var target = $(e.target);
                 if (target.parent('.page-sidebar').length) {
                     return;
                 }
             }
             if (_this.$body.hasClass('menu-pin'))
                 return;

             if ($('.sidebar-overlay-slide').hasClass('show')) {
                 $('.sidebar-overlay-slide').removeClass('show')
                 $("[data-pages-toggle']").removeClass('active')

             }

             _this.$element.css({
                 'transform': menuClosedCSS
             });
             _this.$body.removeClass('sidebar-visible');
         }


         this.$element.bind('mouseenter mouseleave', sidebarMouseEnter);
         this.$pageContainer.bind('mouseover', sidebarMouseLeave);

         function toggleMenuPin(){
           var width = $(window).width();
           if(width < 1200){
             if($('body').hasClass('menu-pin')){
               $('body').removeClass('menu-pin')
               $('body').addClass('menu-unpinned')
             }
           } else {
             if($('body').hasClass('menu-unpinned')){
               $('body').addClass('menu-pin')
             }
           }
         }
         toggleMenuPin();
         $(document).bind('ready', toggleMenuPin);
         $(window).bind('resize', toggleMenuPin);

     }


     // Toggle sidebar for mobile view
     Sidebar.prototype.toggleSidebar = function(toggle) {
         var timer;
         var bodyColor = $('body').css('background-color');
         $('.page-container').css('background-color', bodyColor);
         if (this.$body.hasClass('sidebar-open')) {
             this.$body.removeClass('sidebar-open');
             timer = setTimeout(function() {
                 this.$element.removeClass('visible');
             }.bind(this), 400);
         } else {
             clearTimeout(timer);
             this.$element.addClass('visible');
             setTimeout(function() {
                 this.$body.addClass('sidebar-open');
             }.bind(this), 10);
             setTimeout(function(){
                // remove background color
                $('.page-container').css({'background-color': ''});
             },1000);

         }

     }

     Sidebar.prototype.togglePinSidebar = function(toggle) {
         if (toggle == 'hide') {
             this.$body.removeClass('menu-pin');
         } else if (toggle == 'show') {
             this.$body.addClass('menu-pin');
         } else {
             this.$body.toggleClass('menu-pin');
         }

     }


     // SIDEBAR PLUGIN DEFINITION
     // =======================
     function Plugin(option) {
         return this.each(function() {
             var $this = $(this);
             var data = $this.data('pg.sidebar');
             var options = typeof option == 'object' && option;

             if (!data) $this.data('pg.sidebar', (data = new Sidebar(this, options)));
             if (typeof option == 'string') data[option]();
         })
     }

     var old = $.fn.sidebar;

     $.fn.sidebar = Plugin;
     $.fn.sidebar.Constructor = Sidebar;


     $.fn.sidebar.defaults = {
         pageContainer: '.page-container'
     }

     // SIDEBAR PROGRESS NO CONFLICT
     // ====================

     $.fn.sidebar.noConflict = function() {
         $.fn.sidebar = old;
         return this;
     }

     // SIDEBAR PROGRESS DATA API
     //===================

     $(document).on('click.pg.sidebar.data-api', '[data-toggle-pin="sidebar"]', function(e) {
         var $this = $(this);
         var $target = $('[data-pages="sidebar"]');
         $target.data('pg.sidebar').togglePinSidebar();
         return false;
     })
     $(document).on('click.pg.sidebar.data-api', '[data-toggle="sidebar"]', function(e) {
        console.log("menu open");
        var $this = $(this);
        var $target = $('[data-pages="sidebar"]');
        $target.data('pg.sidebar').toggleSidebar();
        return false
    })

 })(window.jQuery);


 /* ============================================================
 * Pages Notifications
 * ============================================================ */

(function($) {

    'use strict';

    var Notification = function(container, options) {

        var self = this;

        // Element collection
        self.container = $(container); // 'body' recommended
        self.notification = $('<div class="pgn push-on-sidebar-open"></div>');
        self.options = $.extend(true, {}, $.fn.pgNotification.defaults, options);

        if (!self.container.find('.pgn-wrapper[data-position=' + this.options.position + ']').length) {
            self.wrapper = $('<div class="pgn-wrapper" data-position="' + this.options.position + '"></div>');
            self.container.append(self.wrapper);
        } else {
            self.wrapper = $('.pgn-wrapper[data-position=' + this.options.position + ']');
        }

        self.alert = $('<div class="alert"></div>');
        self.alert.addClass('alert-' + self.options.type);

        if (self.options.style == 'bar') {
            new BarNotification();
        } else if (self.options.style == 'flip') {
            new FlipNotification();
        } else if (self.options.style == 'circle') {
            new CircleNotification();
        } else if (self.options.style == 'simple') {
            new SimpleNotification();
        } else { // default = 'simple'
            new SimpleNotification();
        }

        // Notification styles
        function SimpleNotification() {

            self.notification.addClass('pgn-simple');

            self.alert.append(self.options.message);
            if (self.options.showClose) {
                var close = $('<button type="button" class="close" data-dismiss="alert"></button>')
                    .append('<span aria-hidden="true">&times;</span>')
                    .append('<span class="sr-only">Close</span>');

                self.alert.prepend(close);
            }

        }

        function BarNotification() {

            self.notification.addClass('pgn-bar');
            self.alert.addClass('alert-' + self.options.type);
            var close = '';
            if (self.options.showClose) {
                close = $('<button type="button" class="close" data-dismiss="alert"></button>')
                    .append('<span aria-hidden="true">&times;</span>')
                    .append('<span class="sr-only">Close</span>');

            }

            if($('body').hasClass("horizontal-app-menu")){
                var container = $('<div class="container"/>');
                container.append('<span>' + self.options.message + '</span>');
                container.append(close);
                self.alert.append(container);
            }
            else{
                self.alert.append(self.options.message);
                self.alert.prepend(close);
            }

        }

        function CircleNotification() {

            self.notification.addClass('pgn-circle');

            var table = '<div>';
            if (self.options.thumbnail) {
                table += '<div class="pgn-thumbnail"><div>' + self.options.thumbnail + '</div></div>';
            }

            table += '<div class="pgn-message"><div>';

            if (self.options.title) {
                table += '<p class="bold">' + self.options.title + '</p>';
            }
            table += '<p>' + self.options.message + '</p></div></div>';
            table += '</div>';

            if (self.options.showClose) {
                table += '<button type="button" class="close" data-dismiss="alert">';
                table += '<span aria-hidden="true">&times;</span><span class="sr-only">Close</span>';
                table += '</button>';
            }


            self.alert.append(table);
            self.alert.after('<div class="clearfix"></div>');

        }

        function FlipNotification() {

            self.notification.addClass('pgn-flip');
            self.alert.append("<span>" + self.options.message + "</span>");
            if (self.options.showClose) {
                var close = $('<button type="button" class="close" data-dismiss="alert"></button>')
                    .append('<span aria-hidden="true">&times;</span>')
                    .append('<span class="sr-only">Close</span>');

                self.alert.prepend(close);
            }

        }

        self.notification.append(self.alert);

        function alignWrapperToContainer(){
            var containerPosition = $(".header").get(0);
            var containerHeight = $(containerPosition).height();

            if(/top/.test(self.options.position)){
              self.wrapper.css('top', containerHeight)
            }
        }

        alignWrapperToContainer()
        $(window).on('resize', alignWrapperToContainer)


        // bind to Bootstrap closed event for alerts
        self.alert.on('closed.bs.alert', function() {
            self.notification.remove();
            self.options.onClosed();
            // refresh layout after removal
        });

        return this; // enable chaining
    };

    Notification.VERSION = "1.0.0";

    Notification.prototype.show = function() {

        // TODO: add fadeOut animation on show as option
        this.wrapper.prepend(this.notification);

        this.options.onShown();

        if (this.options.timeout != 0) {
            var _this = this;
            // settimeout removes scope. use .bind(this)
            setTimeout(function() {
                this.notification.fadeOut("slow", function() {
                    $(this).remove();
                    _this.options.onClosed();
                });
            }.bind(this), this.options.timeout);
        }

    };

    $.fn.pgNotification = function(options) {
        return new Notification(this, options);
    };

    $.fn.pgNotification.defaults = {
        style: 'simple',
        message: null,
        position: 'top-right',
        type: 'info',
        showClose: true,
        timeout: 4000,
        onShown: function() {},
        onClosed: function() {}
    }
})(window.jQuery);


(function($) {
    'use strict';
    // Initialize layouts and plugins
    (typeof angular === 'undefined') && $.Pages.init();
})(window.jQuery);