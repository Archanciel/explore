def action1( **args ):
	print('action1')
	print(args)
	
def run_this_test(function_name, **args):
	print("run_this_test")
	function_name(f=args['l'])
	
run_this_test(action1, f='harry', l= 'potter')