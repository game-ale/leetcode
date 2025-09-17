var interpret = function(command) {
	return command.replace(/(\(\))|(\(al\))/g, (str) => {
		return str === '()' ? 'o' : 'al';
	});
};