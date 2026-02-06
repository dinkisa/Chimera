{  
  "name": "fetch_trends",  
  "description": "Fetches trending topics from a social media platform.",  
  "inputSchema": {  
    "type": "object",  
    "properties": {  
      "platform": {  
        "type": "string",  
        "enum": ["twitter", "instagram"]  
      }  
    },  
    "required": ["platform"]  
  },  
  "outputSchema": {  
    "type": "array",  
    "items": {  
      "type": "string"  
    }  
  }  
}  