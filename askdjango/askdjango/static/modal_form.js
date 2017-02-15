(function() {
    var $modal_form = null;

    var new_modal_form = function($html, $target) {
        $modal_form = $html;
        $modal_form.modal();

        // $modal_form 내 form네 대해 ajaxForm 세팅
        $modal_form.find('form').ajaxForm(function(response_text) {
            $modal_form.modal('hide');

            var $ele = $(response_text);
            var is_new_modal_form = ($ele.find('form').size() > 0);

            // 오류응답일 경우, 다시 Form을 띄운다.
            if ( is_new_modal_form ) {
                new_modal_form($ele, $target);
            }
            // 정상응답일 경우, $target에 HTML을 갱신
            else {
                $target.html(response_text);
            }
        });
    };

    $(document).on('click', '.ajax-modal-form', function() {
        var url = $(this).attr('href');
        var target_id = $(this).data('target-id');
        var $target = $('#' + target_id);
        $.get(url).done(function(html) {
            new_modal_form($(html), $target);
        });
        return false;
    });
})();
