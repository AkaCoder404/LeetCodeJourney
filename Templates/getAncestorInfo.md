<%*

	// get path (relative to vault) for current note 
	const notePath = tp.file.path(true); 
	
	// get TAbstractFile for current note 
	let tFile = this.app.vault.getAbstractFileByPath(notePath); 
	
	// get all parents and output their names to the template engine replacement string tR 
	tR = ""; 
	
	// while (!tFile.parent?.isRoot()) { 
	//    tR = "[[" + tFile.parent.name + "]] | " + tR; 
	 //   tFile = tFile.parent; 
	// } 

	while (!tFile.parent?.isRoot()) { 
	   tR = tFile.parent.name + " | " + tR; 
	   tFile = tFile.parent; 
	} 

	// tR = "File Hiearchy: " + tR;
	
	// remove last pipe and blank characters from output 
	tR = tR.slice(0, -2); 

_%>
