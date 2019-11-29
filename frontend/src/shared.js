export default {
    getTimeStamp(utctime) {
        if (utctime === undefined) {
            return ''
        }
        var datetime = new Date(utctime);
        var date = datetime.toLocaleDateString();
        var time = datetime.toLocaleTimeString();
        return '(' + date + ' ' + time + ')'
    },
}
