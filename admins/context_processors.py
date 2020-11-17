def add_variable_to_context(request):
    try:
        username = request.session['username']
        
        return {
                 'homename': username,
            }
        
    except:
        return {}