const express = require('express'); 
const app = express(); 
app.use(express.json()); 
 
app.post('/resume-review', (req, res) =
    const { resume_text } = req.body; 
    if (!resume_text) { 
        return res.status(400).json({ error: "No resume text provided" }); 
    } 
 
    const response = { 
        feedback: { 
            missing_sections: ["Certifications", "Projects"], 
            keyword_suggestions: ["Cloud Computing", "Machine Learning"], 
            resume_score: 7.5 
        } 
    }; 
    res.json(response); 
}); 
 
app.listen(3000, () =
