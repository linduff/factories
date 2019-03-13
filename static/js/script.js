var NameRegEx = /^[a-z0-9]+$/i;
var NumRegEx = /^\d+$/;

function addFactory() {
	document.getElementById("addFactory").style.display = "block";
	closeEditFactory();
	closeDeleteFactory();
}

function closeAddFactory() {
	document.getElementById("addFactory").style.display = "none";
}


function editFactory() {
	document.getElementById("editFactory").style.display = "block";
	closeAddFactory();
	closeDeleteFactory();
}

function closeEditFactory() {
	document.getElementById("editFactory").style.display = "none";
}


function deleteFactory() {
	document.getElementById("deleteFactory").style.display = "block";
	closeAddFactory();
	closeEditFactory();
}

function closeDeleteFactory() {
	document.getElementById("deleteFactory").style.display = "none";
}

// converts the factory names string to a javascript list
function stringtolist() {
	var name_list = '{{ factory_name_list }}';
	
	var names = [];
	var temp_name = "";
	var i = 0;
	while(i < name_list.length){
		if(name_list[i] == ";" && NameRegEx.test(name_list[i+1])) {
			i++;
			while(NameRegEx.test(name_list[i])){
				temp_name += name_list[i];
				i++;
			}
			names.push(temp_name);
			temp_name = "";
		}
		i++;
	}
	return names;
}

// validates that the add form is logically sound
function validateadd() {
	var alertString = "";
	var flag = 0;

	var name = document.forms["addform"]["name"].value;
	var mi = parseInt(document.forms["addform"]["minimum"].value);
	var ma = parseInt(document.forms["addform"]["maximum"].value);
	var numchildren = parseInt(document.forms["addform"]["children"].value);
	
	var names = stringtolist();

	n = 0;
	while(n < names.length) {
		if(!(name.localeCompare(names[n]))){
			alertString += name + " is already a factory\n";
			flag = 1;
			break;
		}
		n++;
	}
	
	if(!(NameRegEx.test(name))) {
		alertString += "Factory Name must only contain letters and numbers\n";
		flag = 1;
	}
	if(!(NumRegEx.test(document.forms["addform"]["minimum"].value))) {
		alertString += "Minimum must be an integer\n";
		flag = 1;
	}
	if(!(NumRegEx.test(document.forms["addform"]["maximum"].value))) {
		alertString += "Maximum must be an integer\n";
		flag = 1;
	}
	if(mi > ma) {
		alertString += "Minimum must be less than or equal to Maximum!\n";
		flag = 1;
	}

	if(!(NumRegEx.test(document.forms["addform"]["children"].value))) {
		alertString += "Children must be an integer\n";
		flag = 1;
	}

	if(numchildren < 1 || numchildren > 15) {
		alertString += "The number of children must be 1-15\n";
		flag = 1;
	}

	if(flag == 1) {
		alert(alertString + "Try again");
		return false;
	}

return true;
}

// validates that the edit form is logically sound
function validateedit() {
	var alertString = ""
	var flag = 0
	var select = document.forms["editform"]["select"].value;
	var mi = document.forms["editform"]["minimum"].value;
	var ma = document.forms["editform"]["maximum"].value;

	var names = stringtolist();

	if(!(NumRegEx.test(document.forms["editform"]["minimum"].value)) && "none".localeCompare(mi)) {
		alertString += "Minimum must be an integer\n";
		flag = 1;
	}
	if(!(NumRegEx.test(document.forms["editform"]["maximum"].value)) && "none".localeCompare(ma)) {
		alertString += "Maximum must be an integer\n";
		flag = 1;
	}

	n = 0;
	while(n < names.length) {
		if(!(select.localeCompare(names[n]))){
			if(flag == 1) {
				alert(alertString + "Try again");
				return false;
			}
			else {
				return true;
			}
		}
		n++;
	}
	if(flag == 1) {
		alert(alertString + select + " is not the name of a current factory\nTry again");
		return false;
	}
	else
		return true;
}

// Validates that the delete form is logically sound
function validatedelete() {
	var select = document.forms["deleteform"]["select"].value;

	var names = stringtolist();

	n = 0;
	while(n < names.length) {
		if(!(select.localeCompare(names[n]))){
			return true;
		}
		n++;
	}
	alert(select + " is not a factory\nTry again");
	return false;

}