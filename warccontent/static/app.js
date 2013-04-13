Ext.application({
    name: 'warccontent',
    appFolder: './',
	controllers: ['WarcContentController'],
    autoCreateViewport: true,
	launch: function() {
		// init app controller
        this.getController('WarcContentController');
    }
});