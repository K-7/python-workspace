jQuery(function() {
	
		var username = "";
		var password = "";
	  
	$( "#popupPanel" ).on({
	    popupbeforeposition: function() {
	        var h = $( window ).height();
	        $( "#popupPanel" ).css( "height", h );
	    }
	});  
	
	//alert box
	var alertBox = function(text,page){
		$('<div>').simpledialog2({
		    mode: 'blank',
		    headerClose: false,
		    callbackClose: function () {
		    				if(page != null)
							{$.mobile.navigate(page);}
		    			 },
		    blankContent : 
		      '<div class="alertBoxContents">'+
		      "<p>" +text+ "</p>"+
		      "<a rel='close' data-role='button' class='alert_close_btn' data-theme='c' data-inline='true' href='#'>Ok</a>"+
		      '</div>'
		 });
	};
	
	$(".field").on("keydown keyup blur",function(){
		$("#message").text("")
		$(".field").removeClass("error")
	});
	
	
	
	$('#save').live("click",function(event){
		event.preventDefault();
		var flag = 0;
		
		if($('#username').val() == "")
		{			
			$('#username').addClass("error")
			flag = 1;
		}
		
		if($('#first_name').val() == "")
		{			
			$('#first_name').addClass("error")
			flag = 1;
		}
		
		
		if($('#password1').val() != $('#password2').val())
		{			
			$('#password1').addClass("error")
			$('#password2').addClass("error")
			$("#message").text("Passwords do not match")
			flag = 1;
		}
		
		
		if ($('#blood').val() == "")
		{
			$('#blood').addClass("error")
			flag = 1;
		}
		if ($('#mobile').val() == "")
		{
			$('#mobile').addClass("error")
			flag = 1;
		}
		
		if ($('#available').val() == "")
		{
			$('#available').addClass("error")
			flag = 1;
		}
		
		var values = {};
		values['username'] = $("#username").val();
		values['first_name'] = $("#first_name").val();
		values['last_name'] = $("#last_name").val();
		
		var l_password = $("#password1").val();
	    values['password'] = l_password
	    values['blood'] = $("#blood").val();
	    values['mobile'] = $("#mobile").val();
	    values['address'] = $("#address").val();
	    values['available'] = $("#available").val();
		values['email'] = $("#email").val();
		values['user_id'] = $("#user_id").val();
		values['gps_position']  = get_gps_position()
		var dataParams = JSON.stringify(values);
		
		if (flag == 0)
		{ 
	    	var url = "http://127.0.0.1:8000/app/register/";
	    	$.ajax({
	            type: "POST",
	            url: url,
	            data: dataParams,
	            success: function(response, request) {
	            	
	                var responseObj = $.parseJSON(response);
	                console.log(responseObj);
	                if(responseObj.status == "success")
	                 { 
	                 	password = l_password
	                 	responseObj.password = password
						localStorage["user_details"] = JSON.stringify(responseObj);
	                	$.mobile.navigate("#search");
	                 }
	                else
	                { //popup indicating the username exists already
	                 }
	                
	            },
	            failure: function(response, request) {
	                console.log('Failure');
	                
	            }
	        });
		}
		else
		{ 
			$("#message").text("Mandatory Fields cant be Empty");
			return false;
		}
	});
	
	
	function get_gps_position () {
	  navigator.geolocation.getCurrentPosition (function (pos)
		{
		  var lat = pos.coords.latitude;
		  var lng = pos.coords.longitude;
		  return (lat,lng);
		});
	}
	
	$("#btn-search").live("click",function(){
		
		if ($('#blood_grp').val() == "")
		{
			$('#blood_grp').addClass("error")
			alertBox("Select the Blood group you want to search",null)
			return false;
		}
		if ($('#area').val() == "")
		{
			$('#area').addClass("error")
			alertBox("Select the Range in which you want to search",null)
			return false;
		}
		
		var values = {};
		values['blood'] = $("#blood_grp").val();
		values['area'] = $("#area").val();
		values['gps_position']  = get_gps_position()
		var dataParams = JSON.stringify(values);
		
		var url = "http://127.0.0.1:8000/app/search/";
	    	$.ajax({
	            type: "POST",
	            url: url,
	            data: dataParams,
	            success: function(response, request) {
	            	var list = "";
	                var responseObj = $.parseJSON(response);
	                
	                if(responseObj.status == "success")
	                 { 
						localStorage["search_details"] = JSON.stringify(responseObj);
						var users = responseObj.user_list;
						
						for(i=0;i<users.length;i++)
						{
							list += "<li data-id="+users[i]["id"]+" data-tel='" +users[i]["mobile_number"]+"'>"
							list += "<img src='css/images/team.png'/>";
			        		list += "<h3>"+users[i]['name']+"</h3>"; 
			        		list += "<p>"+users[i]['mobile']+"</p>";
			        		list += "</li>";
						}
						$("#ul-lead-list").empty();
	                	$("#ul-lead-list").append(list).listview('refresh');
	                 }
	                else
	                { 
						alertBox("No Users found with this Blood Group in this Area",null)
	                 }
	                
	            },
	            failure: function(response, request) {
	                console.log('Failure');
	                
	            }
	        });	
		
	});

	
	  
	  $("#btn-update-profile").live("click",function(){
	  		$.mobile.navigate("#register");
	  });
	  
	  $("#register").on("pagebeforeshow", function(event, ui) {
	  	
	  	if($.parseJSON(localStorage["user_details"]))
		{
			
			var user = $.parseJSON(localStorage["user_details"])
			$("#user_id").val(user.id)
			$("#name").val(user.name)
			
			$("#blood").val(user.blood).attr('selected', true).siblings('option').removeAttr('selected');
			$("#blood").selectmenu();
			$("#blood").selectmenu("refresh", true);
			
			$("#mobile").val(user.mobile);
			$("#address").val(user.address);
			$("#email").val(user.email);
			
			
			$("#availability_block").css("display","none");
			$("#password1_block").css("display","none");
			$("#password2_block").css("display","none");
			
			$("#register_bck").attr("href","#search");
			
		}
		else
		{
			$("#register_bck").attr("href","#login");
		}
	  })
	  
	  $("#login").live("pageinit",function(event, ui) {
	  		
	  		if($.parseJSON(localStorage["user_details"]))
			{
				$.mobile.navigate("#search");
			}
	  		
	  });
	  
	  $("#btn-logout").live("click",function() {
	  	    
	  		localStorage.clear();
	  		username = "";
			password = "";
	  		// window.location.reload();
	  		alertBox("Sucessfully Logged out !!","#login")
	  });
	  
	  
	  //login btn clicked
	  $("#btn-login").click(function() {
	        
	        
	        var l_username = $("#login_username").val();
	        var l_password = $("#login_password").val();
	        
	        if(l_username == "" || l_username == null) {
	        	alertBox("Please enter Username",null);
	        	return;
	        }
	        if(l_password == "" || l_password == null) {
	        	alertBox("Please enter Password",null);
	        	return;
	        }
	        
	        var values = {};
	        values['username'] = l_username;
	        values['password'] = l_password;
	        var dataParams = JSON.stringify(values);
	        
	        var url = "http://127.0.0.1:8000/app/login/";
	        $.ajax({
	            type: "POST",
	            url: url,
	            data: dataParams,
	            success: function(response, request) {
	            	
	                var responseObj = $.parseJSON(response);
	                
	                if(responseObj.status == "success")
	                 { 
	                 	password = l_password
	                 	responseObj.password = l_password
						localStorage["user_details"] = JSON.stringify(responseObj);
	                	alertBox("Successfully Logged in ..!!","#search");
	                 }
	                else
	                { 
	                  alertBox(responseObj.reason_for_fail,null);
	                 }
	                
	            },
	            failure: function(response, request) {
	                console.log('Failure');
	                
	            }
	        });	
	   });
	   
	  $("#change_pswd").live('pagebeforeshow', function(event) {

		$("#old_password").val("");
		$("#new_password").val("");
		$("#confirm_password").val("");
	  });
	
	 $("#password_update").live("click",function(){
			old_password = $.trim($("#old_password").val());
	        new_password = $.trim($("#new_password").val());
	        confirm_password = $.trim($("#confirm_password").val());			
	        
	        if(old_password == "") {
	        	alertBox("Please enter Old password",null);
	        	return;	
	        }
	        if(new_password == "") 	
	        {
	        	alertBox("Please enter New password",null);
	        	return;
	        }
	        if(confirm_password == "") 	
	        {
	        	alertBox("Please enter Confirm password",null);
	        	return;
	        }
	        
	        if(old_password != password) 	
	        {
	        	alertBox("Please enter correct 'Old password'",null);
	        	return;
	        }
	        if(new_password != confirm_password) 	
	        {
	        	alertBox("Two passwords does not match",null);
	        	return;
	        }
	        
	        
	        if(old_password == new_password) 	
	        {
	        	alertBox("Please choose another password,Old password and New password cannot be the same",null);
	        	return;
	        }
	        else
	        {
	        	var values = {};
		        values["username"] = username;
		    	values["password"] = old_password;
		        values['new_password'] = new_password;
		        
		        var dataParams = JSON.stringify(values);
		        
				var url = "http://127.0.0.1:8000/app/change_pass/";
		        $.ajax({
		            type: "POST",
		            url: url,
		            data: dataParams,
		            success: function(response, request) {
		            	
		                var responseObj = $.parseJSON(response);
		                
		                if(responseObj.status == "success")
		                 { 
		                 	password = new_password;
		                	alertBox("Password successfully changed ..!!","#search");
		                 }
		                else
		                { 
		                  alertBox(responseObj.reason_for_fail,null);
		                 }
		                
		             }
		        });	
	        }
	        
	 });
	
	
	$.mobile.initializePage();

});
