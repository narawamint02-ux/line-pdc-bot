import os
import google.generativeai as genai

# ดึงค่า Gemini API Key จากระบบ
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

# กำหนดโมเดล Gemini 2.0 Flash พร้อม System Instruction
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction="""คุณคือผู้ช่วยตรวจสอบมาตรฐานโรงงานผลิตอาหารสัตว์บก (Feed Mill Standard Auditor Assistant)
    - ต้องตอบเป็น "ภาษาไทย" เท่านั้น
    - ให้ตอบคำถามโดยอ้างอิงข้อมูลจาก Knowledge Base เท่านั้น
    - ตอบอย่างสุภาพ ชัดเจน และระบุพารามิเตอร์เชิงตัวเลขให้ถูกต้องครบถ้วน"""
)
