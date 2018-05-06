from django.contrib import messages


################################################################################
# Exposed
################################################################################

def flash_alert(request,type,text):
	'''
	(obj,str,str)->void
	Creates a bootstrap flash message alert for parameters
	'''
	if (type=="debug"):
		messages.debug(request, text,extra_tags='alert alert-primary')
	elif(type=="info"):
		messages.info(request, text,extra_tags='alert alert-info')
	elif(type=="success"):
		messages.success(request, text,extra_tags='alert alert-success')
	elif(type=="warning"):
		messages.warning(request, text,extra_tags='alert alert-warning')
	elif(type=="error"):
		messages.error(request, text,extra_tags='alert alert-danger')
		return
	else:
		return

################################################################################




################################################################################
# Hidden
################################################################################