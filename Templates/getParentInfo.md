<%*

	// get path (relative to vault) for current note 
	const notePath = tp.file.path(true); 
	
	// get TAbstractFile for current note 
	let tFile = this.app.vault.getAbstractFileByPath(notePath); 
	
	// get first parent
	
	tR = tFile.parent.name;
	tFile = tFile.parent;
	

_%>
