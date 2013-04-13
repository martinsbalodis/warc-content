Ext.define('warccontent.store.Links', {
	extend: 'Ext.data.TreeStore',
	model: 'warccontent.model.Link',
    proxy: {
        noCache: false,
        type: 'ajax',
        url: '/links/'
    }
});