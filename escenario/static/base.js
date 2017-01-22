(function ($, manager) {

    manager.ListManager = function () {
        var self = this;

        self.method = 'GET';

        self.getEscenarios = function (ordering, page, no_wait) {
            self.data = [];

            var ajax_params = {
                async: no_wait,
                method: self.method,
                url: manager.urls.listEscenarios,
                data: {
                    order_by: ordering,
                    page: page
                },
                success: function (result) {
                    self.data = result;
                },
                error: function (result) {
                    alert('error =(');
                },
                dataType: 'json'
            };
            $.ajax(ajax_params);
            return self.data;
        };

        self.getMicroblogPosts = function (page, no_wait) {
            self.data = [];

            var ajax_params = {
                async: no_wait,
                method: self.method,
                url: manager.urls.listMicroblogPosts,
                data: {
                    page: page
                },
                success: function (result) {
                    self.data = result;
                },
                error: function (result) {
                    alert('error =(');
                },
                dataType: 'json'
            };
            $.ajax(ajax_params);
            return self.data;
        }
    };

    manager.RecentShowcase = function () {
        var self = this;

        self.showRecent = function (data, container_id) {
            var container = $(container_id);
            container.empty();
            $.each(data, function (index, item) {
                var _item = '<br><br>' +
                           '<a target="_blank" href="' +
                           item.image_url +
                           '"><img width=300 src="' +
                           item.image_url +
                           '"  alt="' +
                           item.title +
                           '" ></a>';
                container.append(_item);
            });
        };
    };

    manager.VotedShowcase = function () {
        var self = this;

        self.showVoted = function (data, container_id) {
            var container = $(container_id);
            container.empty();
            $.each(data, function (index, item) {
                var _item = '<br><br>' +
                           '<a target="_blank" href="' +
                           item.image_url +
                           '"><img width=300 src="' +
                           item.image_url +
                           '"  alt="' +
                           item.title +
                           '" ></a>' +
                           '<span style="font-size:36px;" id="span' +
                           item.id +
                           '">' + item.votes +
                           '</span>' +
                           '<input type="button" class="vote-button" id="' +
                           item.id +
                           '" value="+1" />';
                container.append(_item);
            });
        };
    };

    manager.MicroblogShowcase = function () {
        var self = this;

        self.showMicroblog = function (data, container_id) {
            var container = $(container_id);
            container.empty();
            $.each(data, function (index, item) {
                var style;
                item.fixed == true ? style = "background-color: #FFE0E0": style = "background-color: #E0E0FF";
                var _item = '<div style="' + style + '">'+ item.text + '</div>';
                container.append(_item);
            });
        };
    };

    manager.CreatorManager = function () {
        var self = this;

        self.method = 'POST';

        self.createEscenario = function (payload, no_wait) {
            self.data = {};
            self.status = 201;

            var ajax_params = {
                async: no_wait,
                method: self.method,
                url: manager.urls.createEscenario,
                data: payload,
                success: function (result, status) {
                    self.data = result;
                    self.status = status;
                },
                error: function (result, status) {
                    alert('error =(');
                    self.status = status;
                },
                dataType: 'json'
            };

            $.ajax(ajax_params);
            return {
                data: self.data,
                status: self.status
            };
        }
    }

})($, window.manager);


