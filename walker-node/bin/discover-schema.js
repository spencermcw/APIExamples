var lookup = require('loopback');
var app = require('../server/server');
var dataSource = app.dataSources.walkerds;

dataSource.discoverModelDefinitions({views: false}, function(err, data) {
    for (var i=0; i<data.length; i++) {
        dataSource.discoverSchema(data[i]['name'], {owner: 'dbo'}, function(err, schema) {
            console.log(JSON.stringify(schema, null, '    '));
        });
    }
});
