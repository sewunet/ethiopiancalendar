
frappe.ui.form.ControlDate = class CustomControlDate extends frappe.ui.form.ControlDate {
   make_input() {
        this.datepicker_eth = true;
        super.make_input();
        this.$ethInput = this.$input.clone();
        this.$ethInput.addClass('hide');
        this.eth_make_picker();
        this._toggleDatepicker();
    }

    show_default_ethiopian() {
        this.datepicker_eth = true;
        this.$ethInput.removeClass('hide');
        this.Input.addClass('hide');
    }

    eth_make_picker() {
        if (typeof $.fn.calendarsPicker === 'function') {
            console.log("Your jQuery Ethiopian calendar function is defined");
        }
        const calendar = $.calendars.instance('ethiopian');
        $(this.$ethInput).calendarsPicker({
            calendar: calendar,
            dateFormat: 'dd-mm-yyyy', // Change the format as needed
            yearRange: 'c-10:c+10',  // Adjusts the year range, similar to ndpYearCount
            onSelect: (dates) => {
                if (dates && dates.length > 0) {
                    const ethDate = dates[0];
                    const jd = ethDate.toJD();
                    console.log(jd);
                    const gregDate = $.calendars.instance('gregorian').fromJD(jd);
                    const formattedDate = gregDate.formatDate(frappe.boot.sysdefaults.date_format);
                    console.log(formattedDate);
                    this.$input.val(formattedDate).trigger('change');
                }
            },
            showOtherMonths: true,
            showAnim: 'fadeIn'
        });
        $(this.$ethInput).removeAttr('readonly');
        this.$input.after(this.$ethInput);
    }
    
    _toggleDatepicker() {
        if (!this.$ethInput || !this.$ethInput.length) { return; }
        if (this.datepicker_eth === true) {
            this.$ethInput.removeClass('hide');
            this.$input.addClass('hide');
        } else {
            this.$input.removeClass('hide');
            this.$ethInput.addClass('hide');
        }
    }
    
    bind_events() {
        this.$wrapper.on('click', '.nd_switch_btn', (ev) => {
            ev.preventDefault();
            ev.stopPropagation();
            this.datepicker_eth = !Boolean(this.datepicker_eth);
            this._toggleDatepicker();
        });
    }
    
    make_wrapper() {
        if (this.only_input) {
            this.$wrapper = $('<div class="form-group frappe-control nd_datepicker_multi"><span class="nd_switch_btn" title="Switch Calendar"></span></div>').appendTo(this.parent);
        } else {
            this.$wrapper = $(`
                <div class="frappe-control nd_datepickers_container">
                    <div class="form-group">
                        <div class="clearfix">
                            <label class="control-label" style="padding-right: 0px;"></label>
                            <span class="help"></span>
                        </div>
                        <div class="control-input-wrapper nd_datepicker_multi">
                            <div class="control-input"></div>
                            <span class="nd_switch_btn" title="Switch Calendar"></span>
                            <div class="control-value like-disabled-input" style="display: none;"></div>
                            <div class="nepali_date-conversion small bold" style="padding-left: 8px;">&nbsp;</div>
                            <p class="help-box small text-muted"></p>
                        </div>
                    </div>
                </div>
            `).appendTo(this.parent);
        }
        this.bind_events();
    }
    
    get_now_date() {
        return frappe.datetime
            .convert_to_system_tz(frappe.datetime.now_date(true), false)
            .toDate();
    }
    
    set_formatted_input(value) {
        console.log(value);
        const spset = super.set_formatted_input(value);
        if (value) {
            const ethDate = this.get_eth_datepicker_format(value);
            this.$ethInput.val(ethDate);
        }
        return spset;
    }
    
    get_eth_datepicker_format(value) {
        try {
            const gregorianCalendar = $.calendars.instance('gregorian');
            const ethCalendar = $.calendars.instance('ethiopian');
            console.log(value);
            // Extract and log date components
            const [day, month, year] = value.split('-').map(Number);
            if (isNaN(day) || isNaN(month) || isNaN(year)) {
                throw new Error('Invalid date components');
            }
            console.log('Day:', day, 'Month:', month, 'Year:', year);
            
            // Create Gregorian date and log it
            const gregDate = gregorianCalendar.newDate(year, month, day);
            console.log('Gregorian Date:', gregDate);
            
            // Convert to Julian Day and then Ethiopian date
            const jd = gregDate.toJD();
            console.log('Julian Day:', jd);
            
            const ethDate = ethCalendar.fromJD(jd);
            console.log('Ethiopian Date:', ethDate);
            
            // Format and return Ethiopian date
            return ethDate.formatDate('dd-mm-yyyy');
        } catch (error) {
            console.error('Error converting date:', error);
            return null;
        }
    }
    
    

    refresh() {
        super.refresh();
        if (!this.can_write()) {
            this.$wrapper.find('.nd_switch_btn').css('display', 'none');
        } else {
            this.$wrapper.find('.nd_switch_btn').css('display', 'block');
        }
    }

   
};
