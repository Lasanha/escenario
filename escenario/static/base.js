(function ($, manager) {

    manager.ListManager = function () {
        var self = this;

        self.method = 'GET';

        self.getEscenarios = function (ordering, page, no_wait) {
            self.data = [];

            var ajax_params = {
                async: no_wait,
                method: self.method,
                url: '/v2/escenarios/',
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
    };

    manager.RecentShowcase = function () {
        var self = this;

        self.showRecent = function (data, container_id) {
            var container = $(container_id);
            container.empty();
            $.each(data, function (index, item) {
                var item = '<br><br>' +
                           '<a target="_blank" href="' +
                           item.image_url +
                           '"><img width=300 src="' +
                           item.image_url +
                           '"  alt="' +
                           item.title +
                           '" ></a>';
                container.append(item);
            });
        };
    };

    manager.VotedShowcase = function () {
        var self = this;

        self.showVoted = function (data, container_id) {
            var container = $(container_id);
            container.empty();
            $.each(data, function (index, item) {
                var item = '<br><br>' +
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
                           '<input type="button" class="vote-button" id=' +
                           item.id +
                           '" value="+1"/>';
                container.append(item);
            });
        };
    };

})($, window.manager);


