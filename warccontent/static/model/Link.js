Ext.define('warccontent.model.Link', {
    extend: 'Ext.data.Model',
    fields: [
		{name: 'id',  type: 'string'},
		{name: 'path',  type: 'string'},
        {name: 'url',  type: 'string'},
        {name: 'childcount', type: 'integer'}
    ]
});