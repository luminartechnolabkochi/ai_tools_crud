from django.shortcuts import render

from django.views.generic import View

from django.http import JsonResponse

from tools.models import AiTool

from django.views.decorators.csrf import csrf_exempt

from django.utils.decorators import method_decorator

from json import loads

@method_decorator(csrf_exempt,name="dispatch")
class AiToolListCreateView(View):

   def get(self,request,*args,**kwargs):
      
      qs = AiTool.objects.all() #type of qs is query set
      #we have to convert qs to PYNT
      result = [{"id":t.id,"name":t.name,"company":t.company,"purpose":t.purpose,"current_version":t.current_version,"category":t.category} for t in qs]

      return JsonResponse({"data":result,"status":"200ok"})
   
   def post(self,request,*args,**kwargs):
      
    #   here request.body is of type json
    # we have to convert json to PYNT
      
      data =loads(request.body)
      """
      data={
        "name":"githubcopilot",
        "company":"micosoft/github",
        "purpose":"code generation",
        "current_version":"gpt-5",
        "category":"coding assistant"
    }

      """
      AiTool.objects.create( name=data.get("name"),
                             company=data.get("company"),
                             purpose=data.get("purpose"),
                             current_version=data.get("current_version"),
                             category=data.get("category")

                            
                            )
      
      return JsonResponse({"data":"created","status":"201 created"})
   
       
    


