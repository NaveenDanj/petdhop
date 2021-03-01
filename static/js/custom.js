jQuery(document).ready(function () {
    (function ($) {

        'use strict';
        /**********************
*Mobile Menu Activatin
***********************/
        var mainMenuNav = $('.main-navigation');
        mainMenuNav.meanmenu({
            meanScreenWidth: '991',
            meanMenuContainer: '.mobile-menu',
            meanMenuClose: '<span class="menu-close"></span>',
            meanMenuOpen: '<span class="menu-bar"></span>',
            meanRevealPosition: 'right',
            meanMenuCloseSize: '0',
        });


        /**********************
     *Sticky Mobile Menu Activatin
     ***********************/
        function stickyMobileMenu() {
            $('.sticky-mobile-menu').on('click', function () {
                $(this).toggleClass('sticky-close');
                $('.sticky-menu').toggleClass('sticky-open');
                $('.sticky-menu').slideToggle('slow');
            });

            $('.sticky-has-child > a').on('click', function (e) {
                e.preventDefault();
                $(this).siblings('ul').slideToggle('slow');
                $(this).siblings('ul').toggleClass('hidden-sub');
            })
            $('.megamenu__heading').on('click', function (e) {
                e.preventDefault();
                $(this).siblings('ul').slideToggle('slow');
                $(this).siblings('ul').toggleClass('hidden-sub');
            })
        }
        stickyMobileMenu();



        /**********************
        *Expand Category Menu
        ***********************/

        function categoryMenuExpand() {
            $(".hidden-menu-item").css('display', 'none');

            $(window).on({
                load: function () {
                    var ww = $(window).width();
                    if (ww <= 1200) {
                        $(".hidden-lg-menu-item").css('display', 'none');
                    }
                },
                resize: function () {

                    var ww = $(window).width();
                    if (ww <= 1200) {
                        $(".hidden-lg-menu-item").css('display', 'none');
                    }
                }
            });


            $("#js-cat-nav-title").on('click', function () {
                $("#js-cat-nav").slideToggle(500);
            });
            $(".js-expand-hidden-menu").on('click', function (e) {
                e.preventDefault();
                $(".hidden-menu-item").toggle(500);
                if (window_width <= 1200) {
                    $(".hidden-lg-menu-item").toggle(500);
                }
                var htmlAfter = "Close Categories";
                var htmlBefore = "More Categories";

                $(this).html($(this).text() == htmlAfter ? htmlBefore : htmlAfter);
                $(this).toggleClass("menu-close");
            });
        }
        /**********************
        *Expand Category Mobile Menu 
        ***********************/

        function categoryMenuExpandInMobile() {
            $('.has-children').on('click', function (e) {
                e.preventDefault();
                $(this).find('.category-nav__submenu').slideToggle('500');
            });
        }
        categoryMenuExpand();
        categoryMenuExpandInMobile();
        /*--
            - Carousel
        ------------------------*/

        var $html = $('html');
        var $body = $('body');
        var $uptimoSlickSlider = $('.petmark-slick-slider');

        /*For RTL*/
        if ($html.attr("dir") == "rtl" || $body.attr("dir") == "rtl") {
            $uptimoSlickSlider.attr("dir", "rtl");
        }

        $uptimoSlickSlider.each(function () {

            /*Setting Variables*/
            var $this = $(this),
                $setting = $this.data('slick-setting') ? $this.data('slick-setting') : '',
                $autoPlay = $setting.autoplay ? $setting.autoplay : false,
                $autoPlaySpeed = parseInt($setting.autoplaySpeed, 10) || 2000,
                $asNavFor = $setting.asNavFor ? $setting.asNavFor : null,
                $appendArrows = $setting.appendArrows ? $setting.appendArrows : $this,
                $appendDots = $setting.appendDots ? $setting.appendDots : $this,
                $arrows = $setting.arrows ? $setting.arrows : false,
                $prevArrow = $setting.prevArrow ? '<button class="' + ($setting.prevArrow.buttonClass ? $setting.prevArrow.buttonClass : 'slick-prev') + '"><i class="' + $setting.prevArrow.iconClass + '"></i></button>' : '<button class="slick-prev">previous</button>',
                $nextArrow = $setting.nextArrow ? '<button class="' + ($setting.nextArrow.buttonClass ? $setting.nextArrow.buttonClass : 'slick-next') + '"><i class="' + $setting.nextArrow.iconClass + '"></i></button>' : '<button class="slick-next">next</button>',
                $centerMode = $setting.centerMode ? $setting.centerMode : false,
                $centerPadding = $setting.centerPadding ? $setting.centerPadding : '50px',
                $dots = $setting.dots ? $setting.dots : false,
                $fade = $setting.fade ? $setting.fade : false,
                $focusOnSelect = $setting.focusOnSelect ? $setting.focusOnSelect : false,
                $infinite = $setting.infinite ? $setting.infinite : false,
                $pauseOnHover = $setting.pauseOnHover ? $setting.pauseOnHover : true,
                $rows = parseInt($setting.rows, 10) || 1,
                $slidesToShow = parseInt($setting.slidesToShow, 10) || 1,
                $slidesToScroll = parseInt($setting.slidesToScroll, 10) || 1,
                $swipe = $setting.swipe ? $setting.swipe : true,
                $swipeToSlide = $setting.swipeToSlide ? $setting.swipeToSlide : false,
                $variableWidth = $setting.variableWidth ? $setting.variableWidth : false,
                $vertical = $setting.vertical ? $setting.vertical : false,
                $verticalSwiping = $setting.verticalSwiping ? $setting.verticalSwiping : false,
                $rtl = $setting.rtl || $html.attr('dir="rtl"') || $body.attr('dir="rtl"') ? true : false;

            /*Responsive Variable, Array & Loops*/
            var $responsiveSetting = typeof $this.data('slick-responsive') !== 'undefined' ? $this.data('slick-responsive') : '',
                $responsiveSettingLength = $responsiveSetting.length,
                $responsiveArray = [];
            for (var i = 0; i < $responsiveSettingLength; i++) {
                $responsiveArray[i] = $responsiveSetting[i];
            }


            /*Slider Start*/
            $this.slick({
                autoplay: $autoPlay,
                autoplaySpeed: $autoPlaySpeed,
                asNavFor: $asNavFor,
                appendArrows: $appendArrows,
                appendDots: $appendDots,
                arrows: $arrows,
                dots: $dots,
                centerMode: $centerMode,
                centerPadding: $centerPadding,
                fade: $fade,
                focusOnSelect: $focusOnSelect,
                infinite: $infinite,
                pauseOnHover: $pauseOnHover,
                rows: $rows,
                slidesToShow: $slidesToShow,
                slidesToScroll: $slidesToScroll,
                swipe: $swipe,
                swipeToSlide: $swipeToSlide,
                variableWidth: $variableWidth,
                vertical: $vertical,
                verticalSwiping: $verticalSwiping,
                rtl: $rtl,
                prevArrow: $prevArrow,
                nextArrow: $nextArrow,
                responsive: $responsiveArray
            });

        });
        /*----------  Dropdown Slide Down Effect  ----------*/

        $(".slide-down--btn").on('click', function (e) {
            e.stopPropagation();
            $(this).siblings('.slide-down--item').slideToggle("400");
            $(this).siblings('.slide-down--item').toggleClass("show");
            var $selectClass = $(this).parents('.slide-wrapper').siblings().children('.slide-down--item');
            $(this).parents('.slide-wrapper').siblings().children('.slide-down--item').slideUp('400');
        })
        /*----------  Slideup While clicking On Dom  ----------*/
        function clickDom() {
            $('body').on('click', function (e) {
                $('.slide-down--item').slideUp('500');
            });
            $('.slide-down--item').on('click', function (e) {
                e.stopPropagation();
            })
        };

        clickDom();



        /*----------  Sticky Header  ----------*/
        function stickyHeader() {

            $(window).on({
                resize: function () {
                    var width = $(window).width();
                    if ((width <= 991)) {
                        $('.sticky-init').removeClass('fixed-header');
                        if ($('.sticky-init').hasClass('sticky-header')) {
                            $('.sticky-init').removeClass('sticky-header');
                        }
                        console.log(width);
                    } else {
                        $('.sticky-init').addClass('fixed-header');
                    }
                },
                load: function () {
                    var width = $(window).width();
                    if ((width <= 991)) {
                        $('.sticky-init').removeClass('fixed-header');
                        if ($('.sticky-init').hasClass('sticky-header')) {
                            $('.sticky-init').removeClass('sticky-header');
                        }
                        console.log(width);
                    } else {
                        $('.sticky-init').addClass('fixed-header');
                    }
                }
            });
            $(window).on('scroll', function () {
                var headerHeight = $('.header')[0].getBoundingClientRect().height;
                if ($(window).scrollTop() >= headerHeight) {
                    $('.fixed-header').addClass('sticky-header');
                }
                else {
                    $('.fixed-header').removeClass('sticky-header');
                }
            });
        }
        stickyHeader()

        /*----------  Range Slider  ----------*/
        $(function () {
            $(".pm-range-slider").slider({
                range: true,
                min: 0,
                max: 500,
                values: [80, 320],
                slide: function (event, ui) {
                    $("#amount").val("$" + ui.values[0] + " - $" + ui.values[1]);
                }
            });
            $("#amount").val("$" + $(".pm-range-slider").slider("values", 0) +
                " - $" + $(".pm-range-slider").slider("values", 1));
        });


        $('.product-view-mode a').on('click', function (e) {
            e.preventDefault();

            var shopProductWrap = $('.shop-product-wrap');
            var viewMode = $(this).data('target');

            $('.product-view-mode a').removeClass('active');
            $(this).addClass('active');
            shopProductWrap.removeClass('grid list').addClass(viewMode);
            if (shopProductWrap.hasClass('grid')) {
                $('.pm-product').removeClass('product-type-list')
            } else {
                $('.pm-product').addClass('product-type-list')
            }
        })



        /*----------  Elevate Zoom  ----------*/

        //initiate the plugin and pass the id of the div containing gallery images
        $("#zoom_03").elevateZoom({ gallery: 'product-view-gallery', cursor: 'pointer', galleryActiveClass: 'active', imageCrossfade: true });

        //pass the images to Fancybox
        $("#zoom_03").bind("click", function (e) {
            var ez = $('#zoom_03').data('elevateZoom');
            // $.fancybox(ez.getGalleryList());
            return false;
        });


        /*----------  Quantity  ----------*/
        $('.count-btn').on('click', function () {
            var $button = $(this);
            var oldValue = $button.parent('.count-input-btns').parent().find('input').val();
            if ($button.hasClass('inc-ammount')) {
                var newVal = parseFloat(oldValue) + 1;
            } else {
                // Don't allow decrementing below zero
                if (oldValue > 0) {
                    var newVal = parseFloat(oldValue) - 1;
                } else {
                    newVal = 0;
                }
            }
            $button.parent('.count-input-btns').parent().find('input').val(newVal);
        });

        /*----------   Shipping Form Toggle   ----------*/

        $('[data-shipping]').on('click', function () {
            if ($('[data-shipping]:checked').length > 0) {
                $('#shipping-form').slideDown();
            } else {
                $('#shipping-form').slideUp();
            }
        })


        /*----------   Add To Cart Animation   ----------*/

        // $('.add-to-cart').on('click', function (e) {

        //     if ($(this).hasClass('added')) {
        //         $(this).removeClass('added').find('i').removeClass('ti-check').addClass('ti-shopping-cart').siblings('span').text('add to cart');
        //     } else {
        //         $(this).addClass('added').find('i').addClass('ti-check').removeClass('ti-shopping-cart').siblings('span').text('added');
        //     }
        // });



        /*----------   Data Background Image   ----------*/
        function bgImageSettings() {
            $('.bg-image').each(function () {
                var $this = $(this),
                    $image = $this.data('bg');

                $this.css({
                    'background-image': 'url(' + $image + ')'
                });
            });
        }

        bgImageSettings();


        /*----------   NIce Select  ----------*/
        $('.nice-select').niceSelect()

        /*----------   Sticky Sidebar  ----------*/
        $('#sidebar').stickySidebar({
            topSpacing: 60,
            bottomSpacing: 60
        });

        /**********************
        *CounterUp activation 
        ***********************/

        $('.counter').counterUp({
            delay: 10,
            time: 3000
        });

        /*----------   Payment method select  ----------*/

        $('[name="payment-method"]').on('click', function () {

            var $value = $(this).attr('value');

            $('.single-method p').slideUp();
            $('[data-method="' + $value + '"]').slideDown();

        });
        $('.slide-trigger').on('click', function () {

            var $value = $(this).data('target');

            // $('.single-method p').slideUp();
            $($value).slideToggle();

        });

        function dropdownAnimation() {
            $('.dropdown').on('show.bs.dropdown', function (e) {
                $(this).find('.dropdown-menu').first().stop(true, true).slideDown(500);
            });

            $('.dropdown').on('hide.bs.dropdown', function (e) {
                $(this).find('.dropdown-menu').first().stop(true, true).slideUp(500);
            });
        }
        dropdownAnimation();




        /* Scroll to Top */


        // When the user clicks on the button, scroll to the top of the document
        $.scrollUp({
            scrollText: '<i class="fas fa-chevron-up"></i>',
            easingType: 'linear',
            scrollSpeed: 900,
        });
    })(jQuery);



    /**********************
  * Countdown Activation
  ***********************/

    $('[data-countdown]').each(function () {
        var $this = $(this), finalDate = $(this).data('countdown');
        $this.countdown(finalDate, function (event) {
            $this.html(event.strftime('<div class="single-countdown"><span class="single-countdown__time">%D</span><span class="single-countdown__text">Days</span></div><div class="single-countdown"><span class="single-countdown__time">%H</span><span class="single-countdown__text">Hrs</span></div><div class="single-countdown"><span class="single-countdown__time">%M</span><span class="single-countdown__text">mins</span></div><div class="single-countdown"><span class="single-countdown__time">%S</span><span class="single-countdown__text">Secs</span></div>'));
        });
    });





    /* Portfolio Filter & Popup Active */
        $('.mesonry-list').imagesLoaded(function () {

            // filter items on button click
            $('.messonry-button').on('click', 'button', function () {
                var filterValue = $(this).attr('data-filter');
                $(this).siblings('.is-checked').removeClass('is-checked');
                $(this).addClass('is-checked');
                $grid.isotope({
                    filter: filterValue
                });
            });

            // init Isotope
            var $grid = $('.mesonry-list').isotope({
                percentPosition: true,
                transitionDuration: '0.7s',
                layoutMode: 'masonry',
                masonry: {
                    columnWidth: '.resizer',
                }
            });

        });





});


