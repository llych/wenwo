/**
 * Created by brianyang on 16-6-28.
 */
function parse_result(opt,data) {
    if (data == 'True') {
        // alert('success!')
        layer.msg(opt+' 成功!');
    } else {
        layer.msg(opt+' 失败!');
        // alert('failed!')
    }
}
function batch_group_opt(group, opt) {
    $.get("/group_batch/" + group + "/" + opt + "/", function (data, status) {
        parse_result(data)
    });
}
function batch_server_opt(server_id, opt) {
    $.get("/server_batch/" + server_id + "/" + opt + "/", function (data, status) {
        parse_result(data)
    });
}
function app_opt(server_id, group, app, opt) {

    $.get(server_id + "/" + group + "/" + app + "/" + opt + "/", function (data, status) {
        
        parse_result(opt,data)
    });
}
function tail_log(server_id, group, app) {
    window.open("/" + server_id + "/" + group + "/" + app + "/tail/")
}
function show_server_status(server_id) {
    $.get("/server/" + server_id + "/status/", function (data, status) {
        $('#server_div').html(data)
    });
}
